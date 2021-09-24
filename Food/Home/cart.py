class cart:
    bucket=[]
    def add_item(self,item):
        self.bucket.append(item)
        return True
    def del_item(self,name):
        for f in self.bucket:
            if f.name==name:
                self.bucket.remove(f)
                break
        return True
    def is_empty(self):
        if len(self.bucket)==0:
            return True
        else:
            return False
    def total_amount(self):
        amount=0
        for f in self.bucket:
            amount+=f.price
        return amount
