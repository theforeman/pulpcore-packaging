# Created by pyp2rpm-3.3.3
%global pypi_name ansible-builder

Name:           python-%{pypi_name}
Version:        0.2.2
Release:        1%{?dist}
Summary:        A tool for building Ansible Execution Environments

License:        Apache-2.0
URL:            https://github.com/ansible/ansible-builder/
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-pyyaml >= 3.12.0
Requires:       python%{python3_pkgversion}-requirements-parser >= 0.2.0
Requires:       python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.md
%{_bindir}/ansible-builder
%{python3_sitelib}/ansible_builder
%{python3_sitelib}/ansible_builder-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 05 2020 Evgeni Golov - 0.2.2-1
- Initial package.
