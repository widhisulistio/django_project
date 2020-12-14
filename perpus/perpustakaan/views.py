from django.shortcuts import render


def buku(request):
    judul = ["Belajar Django", "Belajar Python", "Belajar Bootstrap"]
    penulis = "widhi"

    konteks = {
        'title': judul,
        'penulis': penulis,
    }
    return render(request, 'buku.html', konteks)


def penerbit(request):
    return HttpResponse('Halaman penerbit')

# Create your views here.
