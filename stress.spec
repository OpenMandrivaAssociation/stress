%define	name stress
%define version 1.0.1
%define release  2

Name:         %name
License:      GPL
Group:        System/Kernel and hardware 
Summary:      A tool which imposes a configurable amount of load on your system
Version:      %version
Release:      %release
BuildRoot:    %{_tmppath}/%{name}-buildroot
Source:       http://weather.ou.edu/~apw/projects/stress/%name-%{version}.tar.gz
URL:          http://weather.ou.edu/~apw/projects/stress/
%description

stress is a tool which imposes a configurable amount of CPU, memory, I/O, or
disk stress on a POSIX-compliant operating system. It is written in
highly-portable ANSI C, and uses the GNU Autotools to compile on a great number
of UNIX-like operating systems.

stress is not a benchmark. It is a tool used by system administrators to
evaluate how well their systems will scale, by kernel programmers to evaluate
perceived performance characteristics, and by systems programmers to expose the
classes of bugs which only or more frequently manifest themselves when the
system is under heavy load. 

%prep
%setup

%build
%configure
%make



%clean
rm -rf $RPM_BUILD_ROOT


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/stress
%{_infodir}/stress.info.*
%{_mandir}/man1/*




%changelog
* Wed Aug 12 2009 Frederik Himpe <fhimpe@mandriva.org> 1.0.1-1mdv2010.0
+ Revision: 415722
- Update to new version 1.0.1

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.18.9-4mdv2009.0
+ Revision: 261209
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.18.9-3mdv2009.0
+ Revision: 253576
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.18.9-1mdv2008.1
+ Revision: 140863
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jan 26 2007 Erwan Velu <erwan@mandriva.org> 0.18.9-1mdv2007.0
+ Revision: 113772
- 0.18.9
- Import stress

* Mon Dec 12 2005 Erwan Velu <erwan@seanodes.com> 0.18.8-1mdk
- 0.18.8

* Sat Jul 02 2005 Lenny Cartier <lenny@mandriva.com> 0.18.6-1mdk
- 0.18.6

* Sat Jun 25 2005 Erwan Velu <erwan@seanodes.com> 0.18.4-1mdk
- 0.18.4

* Thu Jan 06 2005 Erwan Velu <erwan@seanodes.com> 0.18.2-1mdk
- Initial rpm

