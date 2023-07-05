## 1/ Qu'est-ce qu'une API ? Donner un exemple d'utilisation d'une API dans un projet.

Une API (Application Programming Interface) est un ensemble de règles et de protocoles qui permettent à différentes applications de communiquer entre elles. Elle définit les méthodes, les formats de données et les conventions à suivre pour échanger des informations de manière standardisée.

Un exemple d'utilisation d'une API dans un projet pourrait être l'intégration d'une API de géolocalisation dans une application de réservation de taxis. L'API de géolocalisation permettrait à l'application de récupérer les coordonnées GPS du client et de les transmettre à l'API pour obtenir la liste des taxis disponibles à proximité. L'API renverrait ensuite les informations sur les taxis disponibles à l'application, qui pourrait les afficher à l'utilisateur pour lui permettre de choisir un taxi et effectuer la réservation.

Dans cet exemple, l'API de géolocalisation fournit une interface standardisée pour accéder aux fonctionnalités de géolocalisation, ce qui permet à l'application de récupérer les informations dont elle a besoin sans avoir à gérer les détails techniques de la géolocalisation elle-même. L'utilisation de l'API facilite l'intégration et la communication entre les différentes parties d'une application.

## 2/ Qu'est-ce qu'un webhook ? Expliquer son fonctionnement et donner un exemple de son utilisation.

Un webhook est un mécanisme de communication utilisé pour envoyer des notifications automatiques et en temps réel d'un système à un autre. Il permet à une application d'envoyer des données ou des événements à une autre application de manière asynchrone, sans qu'il soit nécessaire d'interroger périodiquement l'API pour vérifier les mises à jour.

Le fonctionnement d'un webhook est le suivant :

L'application qui souhaite envoyer des notifications (appelée l'émetteur) enregistre une URL de webhook fournie par l'application destinataire.
Lorsqu'un événement se produit dans l'application émettrice, celle-ci envoie une requête HTTP POST à l'URL de webhook en incluant les données ou les informations liées à l'événement.
L'application destinataire (le récepteur) reçoit la requête HTTP POST sur son URL de webhook et peut alors traiter les données reçues selon ses besoins.
Un exemple d'utilisation d'un webhook est dans un système de notifications en temps réel. Par exemple, dans une application de messagerie instantanée, lorsqu'un utilisateur reçoit un nouveau message, l'application peut utiliser un webhook pour envoyer une notification instantanée à l'utilisateur, l'informant de l'arrivée d'un nouveau message. L'application émettrice envoie les détails du message (expéditeur, contenu, etc.) à l'URL de webhook en tant que requête POST, et l'application destinataire, qui gère les notifications, reçoit cette requête, traite les données et envoie la notification appropriée à l'utilisateur.

Grâce aux webhooks, les applications peuvent communiquer en temps réel et fournir des mises à jour instantanées, ce qui améliore l'expérience utilisateur et permet une intégration plus étroite entre différents systèmes.

## 3/ Quelle est la différence entre une base de données relationnelle et une base de données non relationnelle ?

Une base de données relationnelle utilise le langage SQL (Structured Query Language) pour organiser les données en tables avec des relations définies, tandis qu'une base de données non relationnelle (NoSQL) stocke les données de manière flexible sans schéma fixe et utilise des langages spécifiques (MongoDB par exemple). Les bases de données relationnelles sont adaptées aux structures de données complexes et garantissent l'intégrité des données grâce à des contraintes de clés étrangères, tandis que les bases de données NoSQL offrent une évolutivité horizontale et une flexibilité accrues pour les applications nécessitant une grande échelle et des schémas de données souples.

## 4/ Déjà utilisé Python ? Explique brièvement ton expérience ou tes connaissances concernant le langage.

J'ai déjà utilisé Python dans le cadre de petits projets. J'ai d'abord acquis une expérience solide en programmation orientée objet (POO) en utilisant PHP et le framework Symfony. Ensuite, j'ai étendu mes compétences à Python. J'ai réalisé plusieurs projets d'entraînement en Python, notamment :
- un script de scraping pour extraire des données à partir d'un site web
- un script simple pour organiser et trier des fichiers et des dossiers. 
- l'utilisation du framework django pour créer une "todo-list" sur une single page application.
Tous ces projets sont sur des repos privés. Je peux vous donner l'accès si vous le souhaitez.
J'apprécie la simplicité et la syntaxe concise de ce langage pour développer efficacement des solutions.

## 5/ Déjà utilisé Wordpress ou Odoo ? Explique brièvement ton expérience ou tes connaissances concernant ces outils.

J'ai utilisé WordPress dans le cadre de la création de mon site web personnel (https://morgan-mathy.com). J'ai principalement travaillé avec l'outil Elementor, qui est un constructeur de pages convivial, pour concevoir et personnaliser mon site. J'ai également acquis des connaissances sur le développement de thèmes personnalisés pour WordPress lors de ma formation. En revanche, je n'ai pas encore utilisé Odoo et je suis ouvert à l'apprentissage de cet outil pour élargir mes compétences professionnelles.