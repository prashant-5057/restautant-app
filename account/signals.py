from django.db.models.signals import m2m_changed
from account.models import User
from django.db.models import F



def favourite_add_remove(sender, instance, reverse, model, *args, **kwargs):
    # print(kwargs)
    _id, = kwargs['pk_set'] if kwargs['pk_set'] else (0,)
    print("in action", kwargs["action"], kwargs['pk_set'])

    if kwargs["action"] == "post_add" and _id:
        model.objects.filter(id=_id).update(total_like=F('total_like')+1)
        
    elif kwargs["action"] == "post_remove" and _id:
        model.objects.filter(id=_id).update(total_like=F('total_like')-1)

    else:
        print("error")

m2m_changed.connect(
    favourite_add_remove, sender=User.like.through,) 



def favourite_menu(sender, instance, reverse, model, *args, **kwargs):
    # print(kwargs)
    _id, = kwargs['pk_set'] if kwargs['pk_set'] else (0,)
    print("in action", kwargs["action"], kwargs['pk_set'])

    if kwargs["action"] == "post_add" and _id:
        model.objects.filter(id=_id).update(total_like=F('total_like')+1)
        
    elif kwargs["action"] == "post_remove" and _id:
        model.objects.filter(id=_id).update(total_like=F('total_like')-1)

    else:
        print("error")

m2m_changed.connect(
    favourite_menu, sender=User.like_menu.through,) 

def favofavourite(sender, instance, reverse, model, *args, **kwargs):
    # print(kwargs)
    _id, = kwargs['pk_set'] if kwargs['pk_set'] else (0,)
    print("in action", kwargs["action"], kwargs['pk_set'])

    if kwargs["action"] == "post_add" and _id:
        model.objects.filter(id=_id).update(total_save=F('total_save')+1)

    elif kwargs["action"] == "post_remove" and _id:
        model.objects.filter(id=_id).update(total_save=F('total_save')-1)

    # else:
    #     print("error")
        
m2m_changed.connect(
    favofavourite, sender=User.save_menu.through,)




