from django.shortcuts import render, HttpResponse
from .models import Projects
 
frontend = [{"icon": "vscode-icons:file-type-html"}, 
            {"icon": "logos:css-3"},
            {"icon": "vscode-icons:file-type-js-official"},
            {"icon": "logos:react"},
            {"icon": "logos:typescript-icon"},
            {"icon": "simple-icons:shadcnui"},
            {"icon": "simple-icons:ghostery"},
            {"icon": "logos:npm-icon"},
            {"icon": "devicon:framermotion-wordmark"},
            {"icon": "devicon:vitejs"},
            {"icon": "logos:react-query-icon"},
            {"icon": "tabler:seo"},
            ]

backend = [{"icon": "logos:nodejs"},
            {"icon": "logos:flask"},
            {"icon": "devicon:supabase"},
            {"icon": "devicon:express"},
            {"icon": "devicon:socketio"},
            {"icon": "devicon:mongodb"},
            {"icon": "logos:typescript-icon"},
            {"icon": "carbon:api-1"},
            {"icon": "devicon:mongoose-wordmark"},
            {"icon": "devicon:postgresql"}
          ]

tools = [   {"icon" :"logos:docker-icon"},
            {"icon": "devicon:swagger"},
            {"icon": "devicon:postman"},
            {"icon": "devicon:figma"},
            {"icon": "devicon:vscode"},
            {"icon": "devicon:github"},
            {"icon": "devicon:git"},
            {"icon": "simple-icons:render"},
            {"icon": "devicon:vercel"},
            {"icon": "simple-icons:hostinger"},
            {"icon": "devicon:netlify"}
          ]

 


def home(request):
    return render(request , "home.html")


 

def projects(request):  
    projects = Projects.objects.all()
    return render(request, "projects.html", {"projects": projects})


def stack(request): 
    return render(request, "stack.html", {"frontend": frontend, "backend": backend, "tools": tools})

def about(request):
    return render(request, "about.html")