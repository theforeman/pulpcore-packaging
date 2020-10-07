# Created by pyp2rpm-3.3.3
%global pypi_name rich

Name:           python-%{pypi_name}
Version:        8.0.0
Release:        1%{?dist}
Summary:        Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal

License:        None
URL:            https://github.com/willmcgugan/rich
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-colorama < 0.5.0
Requires:       python3-colorama >= 0.4.0
Requires:       python3-commonmark < 0.10.0
Requires:       python3-commonmark >= 0.9.0
Requires:       python3-dataclasses < 0.8
Requires:       python3-dataclasses >= 0.7
Requires:       python3-ipywidgets < 8.0.0
Requires:       python3-ipywidgets >= 7.5.1
Requires:       python3-pygments < 3.0.0
Requires:       python3-pygments >= 2.6.0
Requires:       python3-typing-extensions < 4.0.0
Requires:       python3-typing-extensions >= 3.7.4

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Oct 07 2020 Ian Ballou 8.0.0-1
- Update to 8.0.0

* Wed Sep 09 2020 Evgeni Golov 6.1.1-1
- Update to 6.1.1

* Tue Sep 01 2020 Evgeni Golov 6.0.0-1
- Update to 6.0.0

* Tue Aug 25 2020 Evgeni Golov - 5.2.1-1
- Initial package.
