from django.shortcuts import render, redirect, reverse
from django.http import HttpRequest
from .models import Chatbot, GeneralQuery, GeneralResponse, ReportQuery, ReportResponse
from .forms import CreateChatbotForm, QueryForm
from uuid import UUID
from django.contrib import messages
from .ai.ai import resp

def index(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect(reverse('login-screen'))
    chatbots = Chatbot.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = CreateChatbotForm(request.POST)
        if form.is_valid():
            if len(chatbots) < 5:
                cbot = Chatbot(user=request.user, name=form.cleaned_data['name'])
                cbot.save()
            else: 
                messages.error(request=request, message="Unfortunately, we don't want too many (more than 5) chatbots to be created. Sorry")
            return redirect(reverse('core-page'))
    else:
        form = CreateChatbotForm()
    return render(request, 'core.html', { 'name': request.user.get_username(), 'chatbots': chatbots, 'form': form })

def get_chatbot_by_id(request: HttpRequest, id: str):
    if not request.user.is_authenticated:
        return redirect(reverse('login-screen'))
    uuid = UUID(id)
    cbot = Chatbot.objects.filter(id=uuid)[0]
    
    if cbot == None:
        messages.error(request="request", message="Chatbot doesn\'t exist!")
        return redirect(reverse('core-page'))
    
    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():
            t = form.cleaned_data['query_choice']
            q = None
            r = None
            format_of_data = form.cleaned_data['format_of_data']
            if t == "general":
                response = resp(form.cleaned_data['query'], t, None)
                q = GeneralQuery(text=form.cleaned_data['query'], bot=cbot)
                r = GeneralResponse(text=response, g_query=q)
            else:
                response = resp(form.cleaned_data['query'], t, format_of_data)
                q = ReportQuery(criteria=form.cleaned_data['query'], type_of_data=format_of_data, bot=cbot)
                r = ReportResponse(text=response[0], file_link=response[1], r_query=q)
            q.save()
            r.save()
            return redirect(reverse('cbot', args=[uuid.hex]))
        else:
            messages.error(request, "Invalid query!")
    else:
        form = QueryForm()
    g_queries = GeneralQuery.objects.filter(bot=cbot)
    r_queries = ReportQuery.objects.filter(bot=cbot)
    queries = []
    for query in g_queries:
        queries.append(query)
    for query in r_queries:
        queries.append(query)
    s_list = sorted(queries, key=lambda q : q.time_created)
    r_list = [GeneralResponse.objects.filter(g_query=q)[0] if type(q) == GeneralQuery
               else ReportResponse.objects.filter(r_query=q)[0] for q in s_list]
    zipped_lists = zip(s_list, r_list)
    return render(request, 
                  'chatbot_page.html', 
                  { 
                    'chatbot': cbot,
                    'form': form,
                    'queries_and_responses': zipped_lists, 
                    'user': request.user.get_username() 
                  })    
