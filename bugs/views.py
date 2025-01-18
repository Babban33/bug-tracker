import io
import base64
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import render
import matplotlib.pyplot as plt
from django.contrib.auth.decorators import login_required

from bugs.models import Bug

@login_required
def bug_trends(request):
    # Get bug counts by date
    bug_counts = Bug.objects.annotate(date=TruncDate('created_at')).values('date').annotate(count=Count('id')).order_by('date')

    # Prepare data for plotting
    dates = [item['date'] for item in bug_counts]
    counts = [item['count'] for item in bug_counts]

    # Create the plot
    plt.figure(figsize=(10, 5))
    plt.plot(dates, counts)
    plt.title('Bug Trends')
    plt.xlabel('Date')
    plt.ylabel('Number of Bugs')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot to a buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the image to base64
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'bugs/bug_trends.html', {'graphic': graphic})