from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse
from django.views import View
import json


from collections import ChainMap


from .models import Seller, BackupHandle


class SellerById(View):

    def get(self, request, seller_id):
        try:
            seller = Seller.objects.get(id=seller_id)

            return JsonResponse({
                'id': seller.id,
                'name': seller.name,
                'handle': seller.handle
            })
        except ObjectDoesNotExist:
            return JsonResponse(status=404, data={'error': 'seller not found'})

    def put(self, request, seller_id):
        try:
            new_handle = json.loads(request.body.decode('utf-8'))

            seller = Seller.objects.get(id=seller_id)
            backup_handle = seller.handle
            backup_handle = BackupHandle.objects.create(
                name_id=seller_id, old_handle=backup_handle, name_user=seller.name)
            seller.handle = new_handle
            seller.save()

            return JsonResponse(status=200, data={'message': 'Updated'})
        except ObjectDoesNotExist:
            return JsonResponse(status=404, data={'error': 'Seller not found'})


class SellerByHandle(View):
    def get(self, request, seller_handle):

        handle_received = request.path.split('/')[4]
        backupHandle = BackupHandle.objects.filter(old_handle=handle_received)

        querySet = []
        for element in backupHandle.values():
            querySet.append(element)

        data = dict(ChainMap(*querySet))

        try:
            backup_handle = BackupHandle.objects.get(id=data['name_id'])

            return JsonResponse({
                'id': backup_handle.name_id,
                'name': backup_handle.name_user,
                'handle': backup_handle.old_handle
            })

        except:

            seller = Seller.objects.get(handle=seller_handle)

            return JsonResponse({
                'id': seller.id,
                'name': seller.name,
                'handle': seller.handle
            })
