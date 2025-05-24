echo off

set script_dir=%~dp0
set frontend_dir=%script_dir%..\streamlit_hierarchy_chart\frontend 

cd %frontend_dir% && npm run build
