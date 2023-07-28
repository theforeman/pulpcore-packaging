%global pypi_name hatch
%{?python_disable_dependency_generator}

Name:           python-%{pypi_name}
Version:        1.7.0
Release:        2%{?dist}
Summary:        Modern, extensible Python project management

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/hatch/
Source:         https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-hatch_vcs
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-tomli


%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:  python%{python3_pkgversion}-click >= 8.0.6
Requires:  python%{python3_pkgversion}-hatchling >= 1.14.0
Requires:  python%{python3_pkgversion}-httpx >= 0.22.0
Requires:  python%{python3_pkgversion}-hyperlink >= 21.0.0
Requires:  python%{python3_pkgversion}-keyring >= 23.5.0
Requires:  python%{python3_pkgversion}-packaging >= 21.3
Requires:  python%{python3_pkgversion}-pexpect >= 4.8
Requires:  python%{python3_pkgversion}-pexpect < 5
Requires:  python%{python3_pkgversion}-platformdirs >= 2.5.0
Requires:  python%{python3_pkgversion}-rich >= 11.2.0
Requires:  python%{python3_pkgversion}-shellingham >= 1.4.0
Requires:  python%{python3_pkgversion}-tomli_w >= 1.0
Requires:  python%{python3_pkgversion}-tomlkit >= 0.11.1
Requires:  python%{python3_pkgversion}-userpath >= 1.7
Requires:  python%{python3_pkgversion}-userpath < 2.0
Requires:  python%{python3_pkgversion}-virtualenv >= 20.16.2



%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{_bindir}/%{pypi_name}

%changelog
* Fri Jul 28 2023 Odilon Sousa <osousa@redhat.com> - 1.7.0-2
- Fix tomli_w requirement

* Wed Jul 26 2023 Odilon Sousa - 1.7.0-1
- Initial package.
