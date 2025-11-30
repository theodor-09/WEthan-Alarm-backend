import random
from datetime import date

def quicksort(tasks, priority_weight=7, days_weight=1):
    if len(tasks) < 2:
        return tasks

    today = date.today()

    def urgency(t):
        return priority_weight * t.priority - days_weight * ((t.due_date.date() - today).days)

    # Cache urgency values so they are not recomputed many times
    u_cache = {id(t): urgency(t) for t in tasks}

    def comes_before(a, b):
        ua, ub = u_cache[id(a)], u_cache[id(b)]
        if ua != ub:
            return ua > ub
        # tie-breakers
        if a.priority != b.priority:
            return a.priority > b.priority
        return a.due_date < b.due_date

    pivot = random.choice(tasks)
    less = []
    greater = []

    for t in tasks:
        if t is pivot:
            continue
        if comes_before(t, pivot):
            less.append(t)
        else:
            greater.append(t)

    return quicksort(less, priority_weight, days_weight) + [pivot] + quicksort(greater, priority_weight, days_weight)
