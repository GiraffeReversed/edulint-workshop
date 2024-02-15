# edulint: config-file=default

# ---- impose_fine ----
# Policista potřebuje pomoct s udělováním pokut. Zašel do baru a zjistil věk
# (age) občana a to, zda pije pivo (beer). Napište funkci
# impose_fine(age, beer), která vrátí True v případě, že občan je nezletilý a
# pije pivo.


def impose_fine(age, beer):
    return False


print("[TEST] impose_fine")
print(f"Expected: {'False':>7} Received: {impose_fine(20, True)}")
print(f"Expected: {'False':>7} Received: {impose_fine(15, False)}")
print(f"Expected: {'True':>7} Received: {impose_fine(17, True)}")
print(f"Expected: {'False':>7} Received: {impose_fine(57, True)}")
print()


# --- count_a ----
# Napište funkci count_a(text), která v řetězci text spočítá počet výskytů
# písmene 'a' (malé i velké písmeno).


def count_a(text):
    return 0


print("[TEST] count_a")
print(f'Expected: {2:>7} Received: {count_a("Abeceda")}')
print(f'Expected: {0:>7} Received: {count_a("slon")}')
print(f'Expected: {1:>7} Received: {count_a("prase")}')
print()


# ---- join ----
# Napište funkci join(text1, text2), která vrátí spojení těchto dvou řetězců,
# přičemž ten kratší z nich bude první.


def join(text1, text2):
    return text1


print("[TEST] join")
print(f'Expected: {"efgabcd":>7} Received: {join("abcd", "efg")}')
print(f'Expected: {"pessova":>7} Received: {join("pes", "sova")}')
print()


# ---- count_zeros ----
# Vstupem v této úloze je table, což je seznam seznamů čísel reprezentujících
# tabulku čísel. Napište funkci count_zeros(table), která vrátí počet nul
# v tabulce.


def count_zeros(table):
    return 0


print("[TEST] count_zeros")
print(f"Expected: {1:>7} Received: {count_zeros([[1, 0], [3, 4]])}")
print(f"Expected: {3:>7} Received: {count_zeros([[3, 0, 0], [0, 12, 3]])}")
print(f"Expected: {0:>7} Received: {count_zeros([[6, 1], [7, 4], [4, 8]])}")
print()


# ---- greatest_common_divisor
# Napište funkci greatest_common_divisor(a, b), která pro zadaná čísla a, b
# vrátí jejich největšího společného dělitele.


def greatest_common_divisor(a, b):
    return 1


print("[TEST] greatest_common_divisor")
print(f"Expected: {12:>7} Received: {greatest_common_divisor(24, 36)}")
print(f"Expected: {1:>7} Received: {greatest_common_divisor(7, 27)}")
print(f"Expected: {16:>7} Received: {greatest_common_divisor(48, 64)}")
print(f"Expected: {1:>7} Received: {greatest_common_divisor(48, 65)}")
