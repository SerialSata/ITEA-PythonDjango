from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls.base import reverse

from .models import Laserapp
from .forms import LaserappForm
from django.conf import settings
from comments.forms import CommentForm
from comments.models import Comment
from comments.views import get_comments_quantity


@login_required(login_url='login')
def index(request):

    try:
        products = Paginator(Laserapp.objects.order_by('name').all(),
                             settings.ITEMS_ON_PAGE).page(request.GET.get('p', 1))
    except (EmptyPage, PageNotAnInteger):
        raise Http404

    return render(request, 'index.html',
                  {
                      'products': products,
                      'comments_count': get_comments_quantity(request)
                  },

                  )


@login_required(login_url='login')
def details(request, slug):
    product = get_object_or_404(Laserapp, slug=slug)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                # author=form.cleaned_data['author'],
                author=request.user,
                body=form.cleaned_data['body'],
                product=product
            )
            comment.save()
            # return redirect(reverse('details', args=[slug]))
            return redirect(product.get_absolute_url())

    return render(request, 'details.html', {'product': product,
                                            # 'comments': Comment.objects.filter(product=product).orderby('-date'),
                                            'form': form,
                                            }
                  )


@login_required(login_url='login')
def edit(request, slug):
    product = get_object_or_404(Laserapp, slug=slug)
    form = LaserappForm(instance=product)
    if request.method == 'POST':
        form = LaserappForm(request.POST, instance=product)
        if form.is_valid():
            form.save
            messages.add_message(
                request, messages.INFO, 'Material has been updated'
            )
    return render(request, 'edit.html', {'form': form})
