from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationCustomForm
import datetime
from django.http import HttpResponse, Http404
from azbankgateways.exceptions import AZBankGatewaysException
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from django.urls import reverse
import logging
from django.shortcuts import render


def userregister(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = UserCreationCustomForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('account:login')
        else:
            form = UserCreationCustomForm()

        context = {'form': form}
        template_name = 'account/registration/register.html'

        return render(request, template_name, context)


def userlogin(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')

        template_name = 'account/registration/login.html'
        return render(request, template_name, {})


def userlogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('account:login')
    else:
        return redirect('/')


def profile(request):
    if request.user.is_authenticated:
        today = datetime.datetime.now()
        context = {'today': today}
        template_name = 'account/profile/profile.html'
        return render(request, template_name, context)
    else:
        return redirect('account:login')


def subscription(request):
    if request.user.is_authenticated:
        context = {}
        template_name = 'account/profile/subscription.html'
        return render(request, template_name, context)
    else:
        return redirect('account:login')


def go_to_gateway_view(request):
    if request.user.is_authenticated:
        amount = 1000
        user_mobile_number = '+989112221234'

        factory = bankfactories.BankFactory()
        try:
            bank = factory.auto_create()
            bank.set_request(request)
            bank.set_amount(amount)
            bank.set_client_callback_url(reverse('account:payment-callback'))
            bank.set_mobile_number(user_mobile_number)

            bank_record = bank.ready()

            return bank.redirect_gateway()
        except AZBankGatewaysException as e:
            logging.critical(e)
            raise e
    else:
        return redirect('account:login')


def callback_gateway_view(request):
    if request.user.is_authenticated:
        tracking_code = request.GET.get(
            settings.TRACKING_CODE_QUERY_PARAM, None)
        if not tracking_code:
            logging.debug("این لینک معتبر نیست.")
            raise Http404

        try:
            bank_record = bank_models.Bank.objects.get(
                tracking_code=tracking_code)
        except bank_models.Bank.DoesNotExist:
            logging.debug("این لینک معتبر نیست.")
            raise Http404

        if bank_record.is_success:
            user = request.user
            user.special = datetime.datetime.now() + datetime.timedelta(days=31)
            user.is_special = True
            user.save()
            template_name = 'account/payment/success.html'
            return render(request, template_name, {})

        return HttpResponse("پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")
    else:
        return redirect('account:login')
