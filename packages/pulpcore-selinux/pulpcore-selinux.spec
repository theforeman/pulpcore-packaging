%define selinux_variants mls strict targeted
%define selinux_modules pulpcore_port pulpcore pulpcore_rhsmcertd
%define debug_package %{nil}

Name:           pulpcore-selinux
Version:        1.2.7
Release:        1%{?dist}
Summary:        SELinux policy for Pulp 3

License:        GPL2+
URL:            https://pulpproject.org
Source0:        https://codeload.github.com/pulp/%{name}/tar.gz/%{version}#/%{name}-%{version}.tar.gz

BuildRequires:  checkpolicy
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd
Requires:       selinux-policy >= %{_selinux_policy_version}
Requires:       pulpcore
Requires(post): policycoreutils, pulpcore
Requires(postun): policycoreutils
%{?systemd_requires}

%description
The SELinux policy for Pulp 3.Y releases.

%prep
%autosetup


%build
for selinuxvariant in %{selinux_variants}
do
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
  for selinuxmodule in %{selinux_modules}
  do
    mv ${selinuxmodule}.pp ${selinuxmodule}.pp.${selinuxvariant}
  done
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done


%install
for selinuxvariant in %{selinux_variants}
do
  install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
  for selinuxmodule in %{selinux_modules}
  do
    install -p -m 644 ${selinuxmodule}.pp.${selinuxvariant} \
      %{buildroot}%{_datadir}/selinux/${selinuxvariant}/${selinuxmodule}.pp
  done
done

%post
for selinuxvariant in %{selinux_variants}
do
  for selinuxmodule in %{selinux_modules}
  do
    /usr/sbin/semodule -s ${selinuxvariant} -i \
      %{_datadir}/selinux/${selinuxvariant}/${selinuxmodule}.pp &> /dev/null || :
  done
done
systemctl daemon-reexec &>/dev/null || :
/sbin/fixfiles -R python3-pulpcore restore || :

%postun
if [ $1 -eq 0 ] ; then
  for selinuxvariant in %{selinux_variants}
  do
    for selinuxmodule in %{selinux_modules}
    do
      /usr/sbin/semodule -s ${selinuxvariant} -r ${selinuxmodule} &> /dev/null || :
    done
  done
  systemctl daemon-reexec &>/dev/null || :
  /sbin/fixfiles -R python3-pulpcore restore || :
fi

%files
%defattr(-,root,root,0755)
%{_datadir}/selinux/*/pulpcore.pp
%{_datadir}/selinux/*/pulpcore_port.pp
%{_datadir}/selinux/*/pulpcore_rhsmcertd.pp


%changelog
* Wed Dec 15 2021 Odilon Sousa <osousa@redhat.com> - 1.2.7-1
- Release pulpcore-selinux 1.2.7

* Tue Oct 26 2021 Evgeni Golov - 1.2.6-2
- Use "pulpcore" to depend on the correct pulpcore,
  regardless of the underlying Python

* Thu Sep 30 2021 Zach Huntington-Meath <zhunting@redhat.com> - 1.2.6-1
- Release pulpcore-selinux 1.2.6

* Wed Aug 25 2021 Odilon Sousa <osousa@redhat.com> - 1.2.5-1
- Release pulpcore-selinux 1.2.5

* Thu Feb 04 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.2.4-1
- Update to 1.2.4

* Fri Nov 27 2020 Evgeni Golov - 1.2.3-2
- reexec systemd after policy changes to make socket labeling work
  this is needed for systemd before 245, where the following bug is fixed
  https://github.com/systemd/systemd/issues/9997

* Tue Nov 03 2020 Evgeni Golov - 1.2.3-1
- Release pulpcore-selinux 1.2.3

* Wed Oct 28 2020 Evgeni Golov - 1.2.2-1
- Release pulpcore-selinux 1.2.2

* Fri Oct 23 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.2.0-1
- Update to 1.2.0

* Wed Oct 14 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.1.4-1
- Update to 1.1.4

* Wed Oct 07 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.1.3-1
- Update to 1.1.3

* Wed Sep 30 2020 Evgeni Golov - 1.1.1-1
- Release pulpcore-selinux 1.1.1

* Tue Sep 29 2020 Evgeni Golov - 1.1.0-1
- Release pulpcore-selinux 1.1.0

* Mon Mar 09 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.0-2
- Bump to build on el8 & define the debug package as null to prevent errors

* Wed Jan 15 2020 Evgeni Golov - 1.0.0-1
- Initial package
