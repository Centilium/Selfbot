[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy) 


! Attention les Selfbots ne sont pas autorisé par Discord alors n'en abusez pas trop ! 

Tutoriel :

1° ouvrir le lien vers Heroku (creez un compte pour les nouveaux sur Heroku est obligatoire)
2° nommez le selfbot et créer l'app 
3° Rendez-vous sur le tableau de bord [![Dashboard Heroku](https://www1.assets.heroku.com/assets/dynos/dyno-dashboard-15bdadc6e59fd3ddacaf546cc055808a0ec56db654aaa03c15639ed0217d2efa.png)](https://dashboard.heroku.com/apps)
4° Rendez-vous sur le selfbot que vous avez créer et allez sur resources et cliquez sur edit de "worker python __init__.py " et activez le Dyno
5° Rendez-vous dans "Settings" et cliquez sur "Reveal Config Vars" et créer "TOKEN" à gauche et à droite collez votre token (qui commence par mfa.) et creez un autre paramètre "PREFIX" à gauche et à droite choissisez votre prefix (souvent : ! ; / .) et une fois ces réglage terminé le selfbot et actif et vous pouvez vous en servir [prefix]aide pour avoir toute les commandes  
