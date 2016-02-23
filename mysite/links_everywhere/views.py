from django.shortcuts import render
from links_everywhere.models import User, URL, Tags


def get_my_saved_links(request):
    errors = []
    if 'email' in request.GET:
        mail_id = request.GET['email']
        if not mail_id:
            errors.append('Please enter a mail id')
            return render(request, 'search_form.html', {'errors': errors})
        else:
            users = User.objects.get(email=mail_id)
            urls = users.url.all()
            urls_and_tags = []
            for url in urls:
                my_urls_tagged = {}
                my_urls_tagged['url'] = url.url
                tags = url.tags.all()
                this_urls_tags = []
                for tag in tags:
                    this_urls_tags.append(tag)
                my_urls_tagged['tags'] = this_urls_tags
                urls_and_tags.append(my_urls_tagged)
            return render(request, 'search_form.html', {'tags_and_urls': urls_and_tags})
    else:
        return render(request, 'search_form.html')
