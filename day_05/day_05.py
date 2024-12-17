inputlines = open('day_05/day_05_input_small.txt').read().splitlines()
print(inputlines)

def get_middle_page_number( updates:list ):
    if len(updates) == 0:
        return None
    return updates[len(updates) // 2]


rules = []
updates = []
isRules = True
for line in inputlines:
    print(line)
    if len(line) == 0:
        print('switch')
        isRules = False
    if isRules:
        rules.append(line)
    else:
        if len(line) > 0:
            updates.append(line)
print('rules')
print(rules)
print('updates')
print(updates)

newrules = []
for rule in rules:
    rule = rule.split('|')
    print(rule)
    newrule = [ int(entry) for entry in rule ]
    newrules.append(newrule)

newupdates = []
for update in updates:
    update = update.split(',')
    print(update)
    newupdate = [ int(entry) for entry in update ]
    newupdates.append(newupdate)


print("------------------------------")
print('newrules')
print(newrules)
print('newupdates')
print(newupdates)

#for each tail of a rule, make a set of things that must come before
#then when traversing an update, for each element, check that it is not in the set of things 

must_come_after = {}
must_come_before = {}
for rule in newrules:
    before = rule[0]
    after = rule[1]
    if before not in must_come_after:
        must_come_after[before] = set()
    must_come_after[before].add(after)
    if after not in must_come_before:
        must_come_before[after] = set()
    must_come_before[after].add(before)

print("must_come_after")
print(must_come_after)
print("must_come_before")
print(must_come_before)

sum_of_middle_pages = 0
updates_to_fix = []
for update in newupdates:
    isValid = True
    added_to_updates_to_fix = False
    seen_pages = set()
    for page in update:
        for seen_page in seen_pages:
            if seen_page in must_come_before:
                if page in must_come_before[seen_page]:
                    isValid = False
                    if not added_to_updates_to_fix:
                        updates_to_fix.append(update)
                        added_to_updates_to_fix = True
        seen_pages.add(page)
    if isValid:
        sum_of_middle_pages += get_middle_page_number(update)

print(sum_of_middle_pages)
print(updates_to_fix)

sum_of_middle_pages = 0
def check_for_valid_update( update: list, should_come_before ):
    isValid = True
    seen_pages = set()
    for page in update:
        for seen_page in seen_pages:
            if seen_page in should_come_before:
                if page in should_come_before[seen_page]:
                    print("in check_for_valid_update, update is", update)
                    # print("in check_for_valid_update, rules are", rules)
                    print("problem with ", page, seen_page)
                    isValid = False
        seen_pages.add(page)
    return isValid

for update in updates_to_fix:
    isValid = False
    seen_pages = set()
    pairs_to_fix = []

    for page in update:
        for seen_page in seen_pages:
            if seen_page in must_come_before:
                if page in must_come_before[seen_page]:
                    isValid = False
                    #find bad rule
                    print(update, seen_page, "must come after", page)
                    pairs_to_fix.append([seen_page, page])
        seen_pages.add(page)
    
    move_to_after = {}
    move_to_before = {}
    print("pairs to fix")
    print(pairs_to_fix)
    for pair in pairs_to_fix:
        before = pair[0]
        after = pair[1]
        if before not in move_to_after:
            move_to_after[before] = set()
        move_to_after[before].add(after)
        if after not in move_to_before:
            move_to_before[after] = set()
        move_to_before[after].add(before)
    while not check_for_valid_update(update, must_come_before):
        for index, page in enumerate(update):
            #page is before some pages that are listed in move_to_after
            print("checking", page, 'at', index)
            if page in move_to_after:
                last_index = index
                print(page, "has move_to_after", move_to_after[page])
                for entry in move_to_after[page]:
                    if update.index(entry) > last_index:
                        last_index = update.index(entry)
                if not last_index == index:
                    #need to move page after the last_index

                    print("last index update")
                    print("updating from", update)
                    print("popping", page, "at", index)
                    update.pop(index)

                    update.insert(last_index, page)
                    print("updated to   ", update)
    #                input("tap to continue....")
                    continue
            # if page in move_to_before:
            #     first_index = index
            #     for entry in move_to_before:
            #         if update.index(entry) < first_index:
            #             first_index = update.index(entry)
            #     if not first_index == index:
            #         #need to move page before the first_index
            #         print("first index update")
            #         print("updating from", update)
            #         print("popping", page, "at", index)
            #         update.pop(index)

            #         update.insert(first_index, page)
            #         print("updated to   ", update)
            #         # input("tap to continue....")
            #         continue


    sum_of_middle_pages += get_middle_page_number(update)

print("new sum of middles", sum_of_middle_pages)
 