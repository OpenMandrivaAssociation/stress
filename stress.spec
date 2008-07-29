%define	name stress
%define version 0.18.9
%define release %mkrel 3

Name:         %name
License:      GPL
Group:        System/Kernel and hardware 
Summary:      A tool which imposes a configurable amount of load on your system
Version:      %version
Release:      %release
BuildRoot:    %{_tmppath}/%{name}-buildroot
Source:       http://weather.ou.edu/~apw/projects/stress/%name-%{version}.tar.bz2
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

%preun
%_remove_install_info %{name}.info

%post
%_install_info %{name}.info

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


