def get_min(arr,i,maximum):
    if i==len(arr)-1:
        return arr[i]
    else:
        minimum=min(arr[i],get_min(arr,i+1,maximum))
    return minimum
    
arr=[12,21,45,78,54,20]
minimum=get_min(arr,0,arr[0])
print(minimum)