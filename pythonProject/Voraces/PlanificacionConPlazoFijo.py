# Conjunto de candidatos: los n trabajos a realizar
# Funcion solucion: cuando se haya planificado todas las tareas
# Funcion de factibilidad: Conjunto T de trabajadores que todabia pueden completar antes de su tope
# Funcion objetivo= maximizar
# Funcion de seleccion: Considerar trabajo en orden decreciente de los beneficios

def getBestItem(data, candidates):
    bestProfit = 0
    bestItem = 0
    for c in candidates:
        profit = data['profit'][c]
    if profit > bestProfit:
        bestProfit = profit
        bestItem = c
    return bestItem


def isFeasible(schedule, nextDate):
    return schedule[nextDate] == -1


def printSol(data, sol):
    print("Task\tProfit\tDate\tDeadline")
    totalProfit = 0
    for i in range(len(sol)):
        task = sol[i]
        if task != -1:
            print(
                str(task) + "\t\t" + str(data['profit'][task]) + "\t\t" + str(i) + "\t\t" + str(data['deadline'][task]))
            totalProfit += data['profit'][task]
        print("PROFIT: " + str(totalProfit))


def greedySchedule(data):
    n = len(data['profit'])
    candidates = set()
    for i in range(n):
        candidates.add(i)
        lastDate = max(data['deadline'])
        schedule = [-1] * (lastDate + 1)
    while candidates:
        bestItem = getBestItem(data, candidates)
        candidates.remove(bestItem)
        i = data['deadline'][bestItem]
        found = False
    while i >= 0 and not found:
        if isFeasible(schedule, i):
            schedule[i] = bestItem
            found = True
            i -= 1
    return schedule


data = {
    'profit': [50, 10, 15, 30],
    'deadline': [2, 1, 2, 1]
}
schedule = greedySchedule(data)
print(schedule)
printSol(data, schedule)
