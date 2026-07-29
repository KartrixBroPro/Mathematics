class Semantic_Network:
    def __init__(self):
        self.triples=[]
    def add(self,subject,predicate,object):
            self.triples.append((subject,predicate,object))
    def query(self,subject=None,predicate=None,object=None,):
            result=[]
            for (s,p,o) in self.triples:
                if (subject is None or subject==s) and (predicate is None or predicate==p) and (object is None or object==o):
                    result.append((subject,predicate,object))
            return result
        
class Frame:
    def __init__(self,name,**slots):
        self.name=name
        self.slots=slots
    def get(self,key):
            return self.slots.get(key,"Unknown")
    def set(self,key,value):
            self.slots[key]=value
    def __repr__(self):
            return f"Frame self.name,self.slots"
        
if __name__=="__main__":
    sn=Semantic_Network()
    sn.add("parrot","is_a","bird")
    sn.add("parrot","has","wings")
    parrot=Frame("Parrot",color="green",legs="2")
    print(parrot.get("color"))
    parrot.set("wings",2)
    print(parrot.get("wings"))