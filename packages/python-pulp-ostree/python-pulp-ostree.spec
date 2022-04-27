%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pulp-ostree

%global prerelease a5
%global prereleaserpm %{?prerelease:.}%{?prerelease}

%global release 5

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.0.0
Release:        %{?prereleaserpm:0.}%{release}%{?prereleaserpm}%{?dist}
Summary:        Ostree plugin for the Pulp Project

License:        GPLv2+
URL:            https://pulpproject.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}%{?prerelease}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools

%description
A Pulp plugin to support hosting ostree repositories.


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulpcore >= 3.15.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pygobject >= 1:3.40.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pygobject < 1:3.41

Requires:       ostree

Provides:       pulpcore-plugin(ostree) = %{version}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}

%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
A Pulp plugin to support hosting ostree repositories.


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}%{?prerelease}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/pulp_ostree
%{python3_sitelib}/pulp_ostree-%{version}%{prerelease}-py%{python3_version}.egg-info


%changelog
* Wed Apr 27 2022 Odilon Sousa <osousa@redhat.com> - 2.0.0-0.5.a5
- Release python-pulp-ostree 2.0.0a5

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.0.0-0.4.a4
- Build against python 3.9

* Thu Jan 27 2022 Evgeni Golov - 2.0.0-0.3.a4
- Update pygobject dependency to include epoch

* Mon Jan 17 2022 Justin Sherrill <jsherril@redhat.com> 2.0.0-0.2.a4
- update to 2.0.0a4

* Thu Dec 02 2021 Justin Sherrill <jsherril@redhat.com> 2.0.0-0.2.a2
- fix pygobject requires

* Wed Oct 20 2021 Justin Sherrill <jsherril@redhat.com> 2.0.0-0.1.a2
- initial build

