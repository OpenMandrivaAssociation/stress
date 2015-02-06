%define	name stress
%define version 1.0.4

Name:         %name
License:      GPL
Group:        System/Kernel and hardware 
Summary:      A tool which imposes a configurable amount of load on your system
Version:      1.0.4
Release:      2
Source0:      http://weather.ou.edu/~apw/projects/stress/%name-%{version}.tar.gz
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
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/stress
%{_infodir}/stress.info.*
%{_mandir}/man1/*
