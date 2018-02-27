#Definition d'une classe avec une property
class Request:
    def __init__(self, id, video, endPoint, nombre):
        self.nb = nombre
        self.endPoint = endPoint
        self.id = id
        self.video = video
        self.distanceActuelle = endPoint.lat_Server

    def __str__(self):
        chaine = "*** Request {}".format(self.id)
        chaine += "\n endpoint :" + str(self.endPoint.id)
        chaine += "\n video :" + str(self.video.id)
        chaine += "\n nb :" + str(self.nb)
        return chaine

    @property
    def size(self):
        return self.video.taille


####Exemple de tri
sorted(self.requests, key=lambda x: x.nb, reverse=True):
#On trie en fonction du nombre

####Exemple de comprehenseion de liste
[c for c in request.endPoint.cacheServeurs if
                             c.free_size(self.max_cap) > request.size and request.video not in c.videos]
#On renvoie les cashserveur sous certaines conditions (taille livre necessaire et video pas dedans


####Pour affichage
logging.info("Adding video " + str(i))


####dict
#https://openclassrooms.com/courses/apprenez-a-programmer-en-python/les-dictionnaires-2
#{},


#### list
#https://openclassrooms.com/courses/apprenez-a-programmer-en-python/les-dictionnaires-2
#[], append, insert, extend, del ma_liste[0], ma_liste.remove(32),
for i, elt in enumerate(ma_liste):
...     print("À l'indice {} se trouve {}.".format(i, elt))
for elt in ma_liste: # elt va prendre les valeurs successives des éléments de ma_liste
...     print(elt)
#https://openclassrooms.com/courses/utilisation-avancee-des-listes-en-python

