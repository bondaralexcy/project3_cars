from celery import shared_task

from vehicle.models import Car, Moto


@shared_task
def check_milage(pk, model):
    if model == 'Car':
        instance = Car.objects.filter(pk=pk).first()
    else:
        instance = Moto.objects.filter(pk=pk).first()

    if instance:
        prev_milage = -1
        for m in instance.milage.all():
            if prev_milage == -1:
                prev_milage = m.milage

            else:
                if prev_milage < m.milage:
                    print("Неверный пробег")
                    break




@shared_task
def my_task():
    # Код задачи
    print("YesYes")

@shared_task
def check_filter():
    filter_price = {"price__lte": 500}

    if Car.objects.filter(**filter_price).exists():
        print("Отчет по фильтру")
    else:
        print("NoNo")

        # send_mail(
        #     subject='Отчет по фильтру',
        #     message='У нас есть машины по вашему запросу, заходите на сайт',
        #     from_email='admin@admin.com',
        #     recepient_list=[user.email]
        # )
