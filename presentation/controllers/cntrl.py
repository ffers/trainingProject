

'''
DTO convert to Domain
      Handler         → Processor → Service → Repository/API
      
Handlers 
Accept already validated DTOs from the controller 
Convert DTO → Domain (or likewise) 
Click on the required Processor/Service

Services 
Implement “pure” operations on one entity 
For example: OrderService.create(order: Order), OrderService.calculateTotal(order) 
Don't know about HTTP, DTO or complex scripts

Processors 
Orchestrate a number of services/repositories/APIs in a complex business process 
For example: 
Enter the database order (OrderService.get) 
Cancel status from external API (ApiClient.fetchStatus) 
Update and save (OrderService.updateStatus) 
Rotate the finished result to the Handler
'''