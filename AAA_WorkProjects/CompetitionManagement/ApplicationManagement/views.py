from django.shortcuts import render

#-------Application Display--------
def application_list(request):
    """Displays the list of all applications. Filtering by status"""
    return render(request, 'application/application_list.html', {})

def application_by(request):
    """Displays the list of all applications for a specific Role.
    Meant to be a 'filteredList_View'"""
    return render(request, 'application/application_byRole.html', {})

def application_detail(request):
    """Detail View on a single Application"""
    return render(request, 'application/application_detail.html', {})

# ----------Process Management ----------------------
def process_overview(request):
    """Managerial Overview displaying the current state of the Review
    process, the associated Assessors and information on the kind and"""
    return render(request, 'review/process_overview', {})

def assessors_overview(request):
    """Assignment and Managing view for the Expert Assessors"""
    return render(request, 'review/assessors_overview.html', {})

def assessors_detail(request):
    """Managerial Detail View on the status, progress and returned review for
    each Expert Assessor."""
    return render(request, 'review/assessors_detail.html', {})

# ---------