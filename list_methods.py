def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    if ticket_type == 0:
        normal_queue.append(person_name)
        return normal_queue
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    raise ValueError ("Invalis Ticket Type")

    


    


def find_my_friend(queue, friend_name):
    if friend_name in queue:
        return queue.index(friend_name)
    """

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """
    pass


def add_me_with_my_friends(queue, index, person_name):
    queue.insert(index, person_name)
    return queue

    """

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """
    pass


def remove_the_mean_person(queue, person_name):
    queue.remove(person_name)
    return queue
    """

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return:  list - queue update with the mean persons name removed.
    """
    pass


def how_many_namefellows(queue, person_name):
    count = 0
    for name in queue:
        if name == person_name:
            count += 1
    return count
    """

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return:  int - the number of times the name appears in the queue.
    """
    pass


def remove_the_last_person(queue):
    a = queue[-1] 
    queue.remove(queue[-1])
    return a
    """

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """
    pass


def sorted_names(queue):
    queue.sort()
    return queue
    """

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """
    pass
