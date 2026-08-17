# promo_run_01.py

# Tagesbericht inhalt
# > Anzahl gewährter und abgewiesener Zugriffe
# > Durchschnittle Freigabestufe der gewährtem Zugriffe(gerundet)
# > Liste der Namen aller abgewiesenen Personen.



check_in_list = [
    ["Noah", 12, "yes"],
    ["Sue", 4, "yes"],
    ["Rick", 1, "no"],
    ["May", 9, "yes"],
    ["Jack",6, "no"]
]



# Anzahl aller gewährten und abgewiesener Zugriffe
total_check_ins = len(check_in_list)
t_granted = 0
t_denied = 0


# Durchschnittle Freigabestufe der gewährtem Zugriffe(gerundet)
c_tier_list = []

for entry in check_in_list:
    if entry[2] == "yes":
        c_tier_list.append(entry[1])
        t_granted += 1


len_c_tier_list = len(c_tier_list)
sum_c_tier_list = sum(c_tier_list)

avg_c_tier_list = sum_c_tier_list / len_c_tier_list




# Liste der Namen aller abgewiesenen Personen.
denied_list = []

for entry in check_in_list:
    if entry[2] == "no":
        denied_list.append(entry[0])
        t_denied += 1



print('\n**** TAGESBERICHT ****')
print('======================\n')
print(f'Heutige Zugriffe: {total_check_ins}')
print(f'Erlaubte Zugriffe: {t_granted}')
print(f'Abgewiesene Zugriffe: {t_denied}\n')
print(f'Durchschn. Freigabestufe: {round(avg_c_tier_list,2)}\n')
print(f'Abgewiesene Personen:\n{denied_list}\n')