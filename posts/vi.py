
def edit(request, id):
    blog = BlogPost.objects.get(id=id)
    form = BlogForm(instance=blog)
    
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            blog = BlogPost(
                title = title,
                content = content
            )
            blog.save()

            return redirect('home')