import wikipediaapi
from django.http import HttpResponseNotFound, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

def get_wikipedia_summary(request):
	title = request.GET.get('title', '')

	wiki_wiki = wikipediaapi.Wikipedia('CoolBot/1.0 (https://example.org/coolbot/; coolbot@example.org)','en')  

	page = wiki_wiki.page(title)

	if page.exists():
		summary = page.summary

		words = summary.split()
		total_words_more_5 = 0
		total_words = len(words)

		for word in words:
			if len(word) >= 5:
				total_words_more_5+=1

		words_percentage = (total_words_more_5/total_words)*100
		if words_percentage > 20:
			subject = 'There are too many words of 5 letters and more in this summary'
			message = 'There are too many words of 5 letters and more in this summary'
			send_mail(subject,message,'bodenanthomas@gmail.com',['thomasbodenan@gmail.com'])

		return HttpResponse(summary+str(words_percentage))
	else:
		return HttpResponseNotFound('Page not found')

def test_email(request):
	subject = 'Test'
	message = 'Ceci est un test'
	sender_email = settings.EMAIL_HOST_USER
	recipient_email = 'thomas.bodenan@edu.devinci.fr'

	send_mail(subject, message, sender_email, [recipient_email])

	return HttpResponse('E-mail envoyé avec succès !')

@api_view(['GET'])
def wiki_stats(request):
    title = request.query_params.get('title')

    if not title:
        return Response({'error': 'Title parameter is missing'}, status=400)

    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(title)

    if page.exists():
        summary = page.summary

        words = summary.split()
        total_words_more_5 = sum(1 for word in words if len(word) >= 5)
        total_words = len(words)
        words_percentage = (total_words_more_5 / total_words) * 100

        if words_percentage > 20:
            subject = 'Excessive Words of 5 or More Letters'
            message = f'The Wikipedia page "{title}" contains excessive words of 5 or more letters.'
            send_mail(subject, message, 'sender@example.com', ['recipient@example.com'])

        response_data = {
            'title': title,
            'summary': summary,
            'words_percentage': words_percentage,
            'total_words': total_words,
            'total_words_more_5': total_words_more_5
        }

        return Response(response_data)
    else:
        return Response({'error': 'Page not found'}, status=404)
