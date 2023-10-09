from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from Tour.models.Package import Package
from Tour.models.payment import Payment
from django.http import JsonResponse
import requests
from Tour.models.Bookings import Booking
from Tour.models.Customer import Customer



class KhaltiRequest(View):
    def get(self, request, package_id):
        package = get_object_or_404(Package, id=package_id)
        context = {
            "package": package,
            "package_id": package_id,
        }
        return render(request, 'Payment.html', context)


class KhaltiVerify(View):
    def get(self, request, package_id):
        token = request.GET.get("token")
        amount = request.GET.get("amount")
        package_id = request.GET.get("package_id")

        url = "https://khalti.com/api/v2/payment/verify/"

        payload = {
            'token': token,
            'amount': amount
        }

        headers = {
            'Authorization': 'key test_secret_key_f642465efd39470fa734081fcdc5f540'
        }
        package = get_object_or_404(Package, id=package_id)
        customer_id = request.session.get('customer')
        customer = get_object_or_404(Customer, id=customer_id)
        response = requests.request("POST", url, headers=headers, data=payload)
        resp_dict = response.json()

        if resp_dict.get("idx"):
            success = True
            payment_id = resp_dict.get("idx")
            payment = Payment(
                package=package,
                payment_id=payment_id,
                token=token,
                amount=amount
            )
            payment.save()

            # Update the Booking record with payment details
            booking = Booking.objects.get(package=package, customer=customer)
            booking.payment_reference = payment_id
            booking.payment_status = 'Success'
            booking.save()
        else:
            success = False

        data = {
            "success": success
        }
        return JsonResponse(data)
