%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

%global pypi_name {{name}}
{% if name != compat_name -%}
%global srcname {{compat_name}}
{% endif %}
Name:           python%{python3_pkgversion}-{{compat_name}}
Version:        {{version}}
Release:        1%{?dist}
Summary:        {{summary}}

License:        {{license}}
URL:            {{url}}
Source0:        {{source}}
{% if not archful %}
BuildArch:      noarch
{% endif %}
BuildRequires:  python%{python3_pkgversion}-devel
{% for br in additional_build_requires -%}
BuildRequires:  {{br}}
{% endfor %}
%{?python_provide:%python_provide python%{python3_pkgversion}-{{compat_name}}}

%description
%{summary}


%prep
set -ex
%autosetup -p1 -n %{pypi_name}-{{pypi_version}}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%generate_buildrequires
%pyproject_buildrequires


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install
{% if top_level_modules -%}
%pyproject_save_files -l {{ top_level_modules }}
{%- else -%}
%pyproject_save_files '*' +auto
{%- endif %}


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python%{python3_pkgversion}-{{compat_name}} -f %{pyproject_files}
{%- if scripts %}
{% for script in scripts %}
%{_bindir}/{{ script }}
{%- endfor %}
{%- endif %}


%changelog
* {{changelog_date}} {{changelog_packager}} - {{version}}-1
- Update to {{version}}
{% if old_changelog %}
{{old_changelog}}
{% endif %}