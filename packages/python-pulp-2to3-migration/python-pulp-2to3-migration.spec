# Created by pyp2rpm-3.3.3
%global pypi_name pulp-2to3-migration

Name:           python-%{pypi_name}
Version:        0.4.0
Release:        1%{?dist}
Summary:        Pulp 2 to Pulp 3 migration tool

License:        GPLv2+
URL:            http://www.pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-django-cursor-pagination
BuildRequires:  python3-jsonschema >= 3.0
BuildRequires:  python3-mongoengine
BuildRequires:  python3-pulpcore < 3.9
BuildRequires:  python3-pulpcore >= 3.6
BuildRequires:  python3-semantic-version
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-django-cursor-pagination
Requires:       python3-jsonschema >= 3.0
Requires:       python3-mongoengine
Requires:       python3-pulpcore < 3.9
Requires:       python3-pulpcore >= 3.6
Requires:       python3-semantic-version
Requires:       python3-setuptools

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/pulp_2to3_migration
%{python3_sitelib}/pulp_2to3_migration-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Oct 07 2020 Ian Ballou - 0.4.0-1
- Initial package.
