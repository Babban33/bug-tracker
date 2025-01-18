import io
import base64
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import get_object_or_404, redirect, render
import matplotlib.pyplot as plt
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from bugs.forms import BugForm, BugSearchForm
from bugs.models import Bug

# @login_required
# def bug_trends(request):
#     # Get bug counts by date
#     bug_counts = Bug.objects.annotate(date=TruncDate('created_at')).values('date').annotate(count=Count('id')).order_by('date')

#     # Prepare data for plotting
#     dates = [item['date'] for item in bug_counts]
#     counts = [item['count'] for item in bug_counts]

#     # Create the plot
#     plt.figure(figsize=(10, 5))
#     plt.plot(dates, counts)
#     plt.title('Bug Trends')
#     plt.xlabel('Date')
#     plt.ylabel('Number of Bugs')
#     plt.xticks(rotation=45)
#     plt.tight_layout()

#     # Save the plot to a buffer
#     buffer = io.BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_png = buffer.getvalue()
#     buffer.close()

#     # Encode the image to base64
#     graphic = base64.b64encode(image_png)
#     graphic = graphic.decode('utf-8')

#     return render(request, 'bugs/bug_trends.html', {'graphic': graphic})

@login_required
def bug_list(request):
    form = BugSearchForm(request.GET)
    bugs = Bug.objects.all()

    if form.is_valid():
        search = form.cleaned_data.get('search')
        status = form.cleaned_data.get('status')
        priority = form.cleaned_data.get('priority')

        if search:
            bugs = bugs.filter(Q(title__icontains=search) | Q(description__icontains=search))
        if status:
            bugs = bugs.filter(status=status)
        if priority:
            bugs = bugs.filter(priority=priority)

    return render(request, 'bugs/bug_list.html', {'bugs': bugs, 'form': form})

@login_required
def create_bug(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.created_by = request.user
            bug.save()
            return redirect('bug_detail', pk=bug.pk)
    else:
        form = BugForm()
    return render(request, 'bugs/create_bug.html', {'form': form})

@login_required
def bug_detail(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    return render(request, 'bugs/bug_detail.html', {'bug': bug})

@login_required
def update_bug(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    if request.method == 'POST':
        form = BugForm(request.POST, instance=bug)
        if form.is_valid():
            bug = form.save()
            return redirect('bug_detail', pk=bug.pk)
    else:
        form = BugForm(instance=bug)