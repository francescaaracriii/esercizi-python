mesi=["gen","feb","mar","apr","mag","giu","lug","ago","set","ott","nov","dic"]
spese=[820,760,910,700,680,1250,890,1420,730,770,800,1100]
budget = 900

for i in range(len(spese)):
    if spese[i]<budget:
         print(mesi[i], spese[i])
         
totale=sum(spese)
print("Totale annuale: ", totale)

media=totale/len(spese)
print(f"Media mensile: {media:.2f}")