from UnorderedList import UnorderedList

def inverterLista(L : UnorderedList):
    anterior = None
    atual = L.head
    while atual != None:
        prox = atual.getNext() #define o próximo pela referência 'next' de atual
        
        atual.next = anterior #redefine referência 'next' de atual para o anterior
        
        anterior = atual #atualiza o anterior para atual
        atual = prox #atualiza o atual para próximo
        
    L.head = anterior
    return L