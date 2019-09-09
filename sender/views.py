from django.http import HttpResponse


def sender(request):
    with open('blacklist.sql', 'rb') as sql:
        response = HttpResponse(sql.read())
        response['content-type'] = 'application/x-sql'
        response['Content-Disposition'] = 'attachment;filename=blacklist.sql'
        return response
