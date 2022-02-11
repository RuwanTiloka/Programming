from tkinter.messagebox import NO


class ConsoleCalculator(object) :
    def __init__(self,num) :
        self.num = num

    def console_calculator(self) :
        self.split = self.num.split()
        self.f_number = int(self.split[0])
        self.m_number = str(self.split[1])
        self.l_number = int(self.split[2])

        self.operator = {
            "+" : self.f_number + self.l_number , 
            "-" : self.f_number - self.l_number , 
            "*" : self.f_number * self.l_number ,
            "/" : self.f_number // self.l_number
        }

        if (self.operator[self.m_number]) :
            print(f"Your answer is : {self.operator[self.m_number]}")

if __name__ == '__main__':
    while(True) :
        result = input("Enter do you want to repeat this programme now ? ")
        if (result == "yes" or result == "y") :
            answer = input("Enter calculator to number (using whitespaces) >> ")
            myCal = ConsoleCalculator(answer)
            myCal.console_calculator()

        else :
            exit()