import random
import sys

def get_py_version():


    return "running on Python {}.{}.{}".format(
        sys.version_info[0],
        sys.version_info[1],
        sys.version_info[2]
    )

def select_action(actions, controllers):
    if len(actions) == 1:
        return actions[0][1]

    actions.reverse()  # in-place

    ctrls = list(controllers)  # make a copy

    while True:
        if len(ctrls) == 0:
            print("weird stuff going down")
            return actions[0][1]  # this should technically not happen

        # find last controller
        ctrl = ctrls.pop()

        # look for messages by this controller in the action queue
        for controller_id, action in actions:
            if controller_id == ctrl:
                return action


def get_unique_controllers(logs):
    return set([l[1] for l in logs])


def remove_inactive(logs, controllers, sockets_pub):
    u_ctrl = get_unique_controllers(logs)

    # make a copy of controllers list so that for loop doesn't get fucky
    for ctrl in list(controllers):
        if ctrl not in u_ctrl:
            controllers.remove(ctrl)

    for sock in list(sockets_pub):
        if sock[0] not in u_ctrl:
            sockets_pub.remove(sock)

def random_id():
    return random.randrange(0,99999)