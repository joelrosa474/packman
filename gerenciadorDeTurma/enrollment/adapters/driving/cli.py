from enrollment.aplication.service.enrollment_service import EnrollmentService
from enrollment.domain.model.student import Student
from enrollment.utils.clean_screen import clean_screen
from enrollment.aplication.service.payment_note_service import PaymentNoteService

class CLI: 
    def __init__(self, enrollmentService: EnrollmentService, paymentService: PaymentNoteService):
        self.enrollmentService = enrollmentService
        self.paymentService = paymentService

    def run(self): 
        while True:
            print("\n=====================Opções=====================")
            print("1--> Fazer inscrição                           |") 
            print("2--> Listar Alunos                             |")
            print("3--> Listar Turmas                             |")
            print("4--> Listar notas de pagamentos                |")
            print("5--> Sair                                      |")
            option = input("\n==>")
            
            clean_screen()
            try:
                if(option == '1'):
                    print("="*100)
                    print(" "*40 ,"Inscrição do aluno")
                    print("="*100)
                    print('\n')
                    
                    name = input("\nDigite o teu nome: ")
                    email = input("Digite o teu email: ")
                    age = int(input("Digite a tua idade: "))
                    
                    self.enrollmentService.enroll(name, email, age)    
                
                if(option == '2'):
                    print("="*130)
                    print(" "*55 ,"Todos os alunos no sistema")
                    print("="*130)
                    print('\n')
                    
                    print(f"{'ID':>0} {'Nome':>32} {'Email':>30} {'Idade':>30} {'Registrado':>30}")
                    print('-' * 130)
                    allStudents = self.enrollmentService.getAllStudents()
                    
                    for student in allStudents:
                        isStudentRegistered = "Não registrado"
                        if not student.classroom_id == None:
                            isStudentRegistered = "Registrado"
                            
                        print(f"{str(student.id):<30} {student.name:<30} {student.email.value():<30} {str(student.age):<24} {isStudentRegistered:<24}")
                        print('-' * 130)
                        
                if(option == '3'):
                    print("="*100)
                    print(" "*40 ,"Turmas do sistema")
                    print("="*100)
                    print('\n')
                    allClassroom = self.enrollmentService.getAllClassroom()

                    for classroom in allClassroom:
                        print('-' * 100)
                        print(f"{'Codigo da turma'} {str(classroom.id):<54} {'Quantidade de Alunos:'} {len(classroom.getStudents())}") 
                        print('-' * 100)
                        
                        print(f"{'ID':>0} {'Nome':>32} {'Email':>30} {'Idade':>30} ")
                        print('-' * 100)
                        
                        for student in classroom.getStudents():
                            print(f"{student.id:<30}{str(student.name):<30} {student.email.value():<30} {str(student.age):<24}")
                            print('-' * 100)
                        
                        print('-' * 100+'\n \n')
                    

                if(option == '4'):
                    print("="*100)
                    print(" "*40 ,"Notas de pagamentos")
                    print("="*100)
                    print('\n')
                    
                    allPaymentNote = self.paymentService.getAllPaymentNote()
                    
                    print(f"{'ID':>0} {'Preço':>39} {'Data de vencimento':>37} {'Estudante':>20} ")
                    print('-' * 110)
    
                    for paymentNote in allPaymentNote:
                        print(f"{paymentNote.id:>0} {paymentNote.price:>32}kz {paymentNote.dueDate:>30} {paymentNote.idStudent:>30} ")
                        print('-' * 110)
                        
                if(option == '5'):
                    print("")
                    break
                
            except ValueError as e:
                print(f"Erro -> ", {e})    
        
            except Exception as e:
                print(f"Erro na Exception", {e})  