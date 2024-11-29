from django.shortcuts import render,HttpResponse
import csv
# Create your views here.
def index(request):
    #return HttpResponse("this is homepage")
    return render(request, 'index.html') 

def classSubmit(request):
    dic={}
    def read_csv_column_wise(csv_file):
        with open(csv_file, "r") as csvfile:
            reader = list(csv.reader(csvfile, delimiter=","))
            n=len(reader)
            m=len(reader[0])
            for col in range(m):
                if reader[0][col]=="ROLL NO":
                    continue
                else:
                    dic[reader[0][col]]=0
            for col in range(m):
                for row in range(1,n):
                    if reader[row][col]=="0":
                        dic[reader[0][col]]+=1
            #print(dic)
    if request.method=="POST":
        course=request.POST.get('course')
        section=request.POST.get('section')
    st= str(course) + "-" + str(section)
    csv_file="lala"
    if(st=="CSM-A"):
        csv_file = "static/Files/CSM-A.csv"
    elif(st=="CSM-B"):
        csv_file = "static/Files/CSM-B.csv"
    elif(st=="CSM-C"):
        csv_file = "static/Files/CSM-C.csv"
    elif(st=="CSB-A"):
        csv_file = "static/Files/CSB.csv"
    elif(st=="CSD-A"):
        csv_file = "static/Files/CSD.csv"
    # dic_var=0
    # for i in dic.values():
    #     dic_var=dic_var+i

    read_csv_column_wise(csv_file)
    #return render(request, 'class.html',{"course":course,"section":section,"result":dic})
    return render(request, 'class.html', {"course":course,"section":section,"result":dic})

def studentSubmit(request):
    lst=[]
    def read_csv_wise(csvfp,rn):
        with open(csvfp, "r") as csvf:
            read = list(csv.reader(csvf, delimiter=","))
            n=len(read)
            m=len(read[0])
            req=0
            for row in range(1,n):
                if read[row][0]==rn:
                    req=row
            for col in range(1,m):
                if read[req][col]=="0":
                    lst.append(read[0][col])
            if len(lst)==0:
                lst.append("No Backlogs")
            # else:
            #     lst.append("No Backlogs")
            #print(lst)
                

    if request.method=="POST":
        crs=request.POST.get('crs')
        sec=request.POST.get('sec')
        rn=request.POST.get('rn')
    s= str(crs) + "-" + str(sec)
    csvfp="lala"
    if(s=="CSM-A"):
        csvfp = "static/Files/CSM-A.csv"
    elif(s=="CSM-B"):
        csvfp = "static/Files/CSM-B.csv"
    elif(s=="CSM-C"):
        csvfp = "static/Files/CSM-C.csv"
    elif(s=="CSB-A"):
        csvfp = "static/Files/CSB.csv"
    elif(s=="CSD-A"):
        csvfp = "static/Files/CSD.csv"
    read_csv_wise(csvfp,str(rn))
    return render(request, 'student.html', {"course":crs,"section":sec,"r":rn,"result":lst})