## Cloud infrastructure

Il team di sviluppo ha rilasciato una nuova web app basata sull'ultima versione di WordPress.

Il tuo compito è creare l'infrastruttura di produzione sulla base di queste indicazioni:

1. Usa AWS come public cloud provider
2. Scegli Apache, Nginx o un altro webserver/servizio AWS per pubblicare il sito su internet
3. I dati devono essere memorizzati in un database MySQL
4. [opzionale] L'infrastruttura dev'essere sicura, tollerante ai guasti e in grado di adattarsi a variazioni di carico
5. [opzionale] Per il provisioning dell'infrastruttura puoi usare lo strumento di IaC che conosci meglio scegliendo tra CloudFormation, Terraform e CDK

Descrivi in un file di testo tutte le componenti dell'infrastruttura e il motivo per cui hai scelto di usarle. Crea un diagramma infrastrutturale con i servizi che compongono l'infrastruttura e i collegamenti tra di essi.



1. Unfortunately, I’ve never worked with AWS and so, currently, I don't have direct experience with implementing a cloud infrastructure with AWS. 

2. As a web server, I would use Nginx, since I have worked with it before. I am familiar with the service's performance and the ability to integrate modules like Fail2Ban, which enhances the service and security.
Additionally, Nginx can function as a proxy, reverse proxy, and load balancer.
The latter feature can be very useful when multiple instances of web servers are available to improve performance and reliability.

3. As mentioned in point 1, I am not familiar with the AWS environment, but after doing some research on the web, I think using Amazon RDS is a good idea for deploying our database.
I like the idea of simplified management, high scalability, excellent performance, and reasonable pricing. 

4. I would follow an approach oriented towards high availability.

5. As mentioned in point 1, I am not familiar with the AWS environment, but after doing some research on the web, I would go with CloudFormation.
This service is provisioned directly bu AWS (AWS-native) which means integration and compatibility with other AWS services.
