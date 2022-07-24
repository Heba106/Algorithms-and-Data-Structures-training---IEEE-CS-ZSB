
def get_optimal_value(capacity, weights, kilo):
    value = 0.
    if capacity==0 or kilo==[]:
        return 0 
    m=kilo.index(max(kilo))
    amount=min(weights[m],capacity)
    value = kilo[m]*amount
    capacity-=amount
    kilo.pop(m)
    weights.pop(m)
    return value + get_optimal_value(capacity, weights, kilo)


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    kilo=[]
    for i in range (len(values)):
        kilo.append(values[i]/weights[i])
    print("{:.10f}".format(get_optimal_value(capacity, weights, kilo)))
  
