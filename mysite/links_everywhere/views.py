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


def get_all_tags_for_url(request):
    errors = []
    if 'link' in request.GET:
        url = request.GET['link']
        if not url:
            errors.append('Enter an url')
            return render(request, 'search_links.html', {'errors':errors})
        else:
            urls = URL.objects.filter(url=url)
            unique_tags = set()
            for url in urls:
                tags = url.tags.all()
                for tag in tags:
                    unique_tags.add(tag)
            return render(request, 'search_links.html', {'unique_tags':unique_tags})
    else:
        return render(request, 'search_links.html')


def get_urls_for_tag(request):
    errors = []
    if 'email' in request.GET:
        if 'tag' in request.GET:
            mail_id = request.GET['email']
            input_tag = request.GET['tag']
            if not mail_id or not input_tag:
                errors.append("Both fields are required")
                return render(request, 'search_tag.html', {'errors':errors})
            else:
                user = User.objects.get(email=mail_id)
                urls = user.url.all()
                tagged_urls = set()
                for url in urls:
                    tags = url.tags.all()
                    for tag in tags:
                        if str(tag) == input_tag:
                            tagged_urls.add(url)
                return render(request, 'search_tag.html', {'tagged_url':tagged_urls})
        else:
            errors.append("Both fields are required")
            return render(request, 'search_tag.html', {'errors':errors})
    else:
        return render(request, 'search_tag.html')



