import heapq
n,m = int (input ("Dados de entrada: "))

H =[]
for j in range (m): #le as arestas do grafo
 a, b, peso = input ().split () #le as arestas de a para b com peso 
 a = int (a) 
 b = int (b) 
 peso = int (peso) 
 heapq.heappush (H, (peso, a, b)) #coloca a aresta no heap
vertices=[[]*n for i in range(n)]    #cria os conjuntos para os n vertices  

for i in range(n):
    vertice[i].append(i) #cada vertice i é inicializado com i
S=[]

for i in range(n):
    S.append(i)   #S(i) é o conjunto ao qual o vertice i pertence
    
count=0
custo=0

while count <n-1:
    peso,a,b =heapq.heappop(H) #remover a proxima arestta do heap
    if S[a] != S[b]:      # se as arestas unem arvores diferentes ...
        custo = custo + c
        p = S[a]
        q = S[b]
        if p<=q:
            p,q = q,p
        for j in C[q]:      #para cada j co conjunto c[q]
            S[j]=p
        C[p].extend(C[q])   #unir c[q] e c[p]  a uniao fica em c[p]
        C[q]= []            #esvazia c[q]
        count = count +1
        print(C)
        print(S)
print(custo)
        
    
