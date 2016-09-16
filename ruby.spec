Name     : ruby
Version  : 2.3.0
Release  : 29
URL      : ftp://ftp.ruby-lang.org/pub/ruby/2.3/ruby-2.3.0.tar.gz
Source0  : ftp://ftp.ruby-lang.org/pub/ruby/2.3/ruby-2.3.0.tar.gz
Summary  : Object Oriented Script Language
Group    : Development/Tools
License  : Ruby MIT TCL
BuildRequires: autoconf
BuildRequires: gdbm-dev
BuildRequires: libffi-dev
BuildRequires: openssl-dev
BuildRequires: yaml-lib
BuildRequires: readline-dev
BuildRequires: zlib-dev
BuildRequires: graphviz
BuildRequires: gmp-dev
BuildRequires: ncurses-dev

Requires: ruby-bin
Requires: ruby-data
Requires: ruby-doc
Requires: ruby-lib
Requires: rubygems
Requires: rubygem-bigdecimal
Provides: /usr/bin/ruby
# Fake provides
Provides: /usr/local/bin/ruby
Patch1: cve-2015-3900.nopatch

%description
A dynamic, open source programming language with a focus on simplicity 
and productivity. It has an elegant syntax that is natural to read and 
easy to write.

%package bin
Summary: bin components for the ruby package.
Group: Binaries

%description bin
bin components for the ruby package.

%package data
Summary: data components for the ruby package.
Group: Data

%description data
data components for the ruby package.

%package dev
Summary: dev components for the ruby package.
Group: Development
Requires: ruby

%description dev
dev components for the ruby package.

%package doc
Summary: doc components for the ruby package.
Group: Documentation

%description doc
doc components for the ruby package.

%package lib
Summary: lib components for the ruby package.
Group: Binaries

%description lib
bin components for the ruby package.

%package -n rubygem-bigdecimal
Summary: This library provides arbitrary-precision decimal floating-point number class.
Group: Development/Tools
Requires: ruby
Requires: rubygems
Provides: rubygem(bigdecimal) = 1.2.8

%description -n rubygem-bigdecimal
This library provides arbitrary-precision decimal floating-point number class.

%package -n rubygem-did_you_mean
Summary: "did you mean?" experience in Ruby: the error message will tell you the right one when you misspelled something. 
Group: Development/Tools
Requires: ruby
Requires: rubygems
Provides: rubygem(did_you_mean) = 1.0.0

%description -n rubygem-did_you_mean
"did you mean?" experience in Ruby: the error message will tell you the right one when you misspelled something.

%package -n rubygem-io-console
Summary: add console capabilities to IO instances. 
Group: Development/Tools
Requires: ruby
Requires: rubygems
Provides: rubygem(io-console) = 0.4.5

%description -n rubygem-io-console
add console capabilities to IO instances.

%package -n rubygem-json
Summary: This is a JSON implementation as a Ruby extension in C. 
Group: Development/Tools
Requires: ruby
Requires: rubygems
Provides: rubygem(json) = 1.8.3

%description -n rubygem-json
This is a JSON implementation as a Ruby extension in C.

%package -n rubygem-minitest
Summary: Minitest provides a complete suite of testing facilities 
Group: Development/Tools
Requires: ruby
Requires: rubygems
Provides: rubygem(minitest) = 5.8.3

%description -n rubygem-minitest
Minitest provides a complete suite of testing facilities

%package -n rubygem-net-telnet
Summary: Provides telnet client functionality.
Group: Development/Tools
Requires: ruby
Requires: rubygems
Provides: rubygem(net-telnet) = 0.1.1

%description -n rubygem-net-telnet
Provides telnet client functionality.

%package -n rubygem-power_assert
Summary: Power Assert for Ruby. 
Group: Development/Tools
Requires: ruby
Requires: rubygems
Provides: rubygem(power_assert) = 0.2.6 

%description -n rubygem-power_assert
Power Assert for Ruby.

%package -n rubygem-psych
Summary: Psych is a YAML parser and emitter. 
Group: Development/Tools
Requires: ruby
Requires: rubygems
Provides: rubygem(psych) = 2.0.17

%description -n rubygem-psych
Psych is a YAML parser and emitter.

%package -n rubygem-rake
Summary: Rake is a Make-like program implemented in Ruby.
Group: Development/Tools
Requires: ruby
Requires: rubygems
Provides: rubygem(rake) = 10.4.2

%description -n rubygem-rake
Rake is a Make-like program implemented in Ruby.

%package -n rubygem-rdoc
Summary: RDoc produces HTML and command-line documentation for Ruby projects.
Group: Development/Tools
Requires: ruby
Requires: rubygems
Requires: rubygem-json
Provides: rubygem(rdoc) = 4.2.1

%description -n rubygem-rdoc
RDoc produces HTML and command-line documentation for Ruby projects.

%package -n rubygem-test-unit
Summary: Improved version of Test::Unit 
Group: Development/Tools
Requires: ruby
Requires: rubygems
Requires: rubygem(power_assert)
Provides: rubygem(test-unit) = 3.1.5

%description -n rubygem-test-unit
Improved version of Test::Unit

%prep
%setup -q -n ruby-2.3.0

%build
%configure \
 --prefix=/usr \
 --enable-shared \
 --disable-rpath \
 --with-dbm-type=gdbm_compat \
 --with-out-ext=tcl \
 --with-out-ext=tk

make V=1 %{?_smp_mflags}

%check
make check TESTS="-v $DISABLE_TESTS" ||:

%install
rm -rf %{buildroot}
%make_install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
/usr/lib64/ruby/2.3.0/English.rb
/usr/lib64/ruby/2.3.0/abbrev.rb
/usr/lib64/ruby/2.3.0/base64.rb
/usr/lib64/ruby/2.3.0/benchmark.rb
/usr/lib64/ruby/2.3.0/cgi.rb
/usr/lib64/ruby/2.3.0/cmath.rb
/usr/lib64/ruby/2.3.0/csv.rb
/usr/lib64/ruby/2.3.0/date.rb
/usr/lib64/ruby/2.3.0/debug.rb
/usr/lib64/ruby/2.3.0/delegate.rb
/usr/lib64/ruby/2.3.0/digest.rb
/usr/lib64/ruby/2.3.0/drb.rb
/usr/lib64/ruby/2.3.0/e2mmap.rb
/usr/lib64/ruby/2.3.0/erb.rb
/usr/lib64/ruby/2.3.0/expect.rb
/usr/lib64/ruby/2.3.0/fiddle.rb
/usr/lib64/ruby/2.3.0/fileutils.rb
/usr/lib64/ruby/2.3.0/find.rb
/usr/lib64/ruby/2.3.0/forwardable.rb
/usr/lib64/ruby/2.3.0/getoptlong.rb
/usr/lib64/ruby/2.3.0/ipaddr.rb
/usr/lib64/ruby/2.3.0/irb.rb
/usr/lib64/ruby/2.3.0/kconv.rb
/usr/lib64/ruby/2.3.0/logger.rb
/usr/lib64/ruby/2.3.0/mathn.rb
/usr/lib64/ruby/2.3.0/matrix.rb
/usr/lib64/ruby/2.3.0/mkmf.rb
/usr/lib64/ruby/2.3.0/monitor.rb
/usr/lib64/ruby/2.3.0/mutex_m.rb
/usr/lib64/ruby/2.3.0/observer.rb
/usr/lib64/ruby/2.3.0/open-uri.rb
/usr/lib64/ruby/2.3.0/open3.rb
/usr/lib64/ruby/2.3.0/openssl.rb
/usr/lib64/ruby/2.3.0/optionparser.rb
/usr/lib64/ruby/2.3.0/optparse.rb
/usr/lib64/ruby/2.3.0/ostruct.rb
/usr/lib64/ruby/2.3.0/pathname.rb
/usr/lib64/ruby/2.3.0/pp.rb
/usr/lib64/ruby/2.3.0/prettyprint.rb
/usr/lib64/ruby/2.3.0/prime.rb
/usr/lib64/ruby/2.3.0/profile.rb
/usr/lib64/ruby/2.3.0/profiler.rb
/usr/lib64/ruby/2.3.0/pstore.rb
/usr/lib64/ruby/2.3.0/resolv-replace.rb
/usr/lib64/ruby/2.3.0/resolv.rb
/usr/lib64/ruby/2.3.0/ripper.rb
/usr/lib64/ruby/2.3.0/rss.rb
/usr/lib64/ruby/2.3.0/scanf.rb
/usr/lib64/ruby/2.3.0/securerandom.rb
/usr/lib64/ruby/2.3.0/set.rb
/usr/lib64/ruby/2.3.0/shell.rb
/usr/lib64/ruby/2.3.0/shellwords.rb
/usr/lib64/ruby/2.3.0/singleton.rb
/usr/lib64/ruby/2.3.0/socket.rb
/usr/lib64/ruby/2.3.0/sync.rb
/usr/lib64/ruby/2.3.0/tempfile.rb
/usr/lib64/ruby/2.3.0/thwait.rb
/usr/lib64/ruby/2.3.0/time.rb
/usr/lib64/ruby/2.3.0/timeout.rb
/usr/lib64/ruby/2.3.0/tmpdir.rb
/usr/lib64/ruby/2.3.0/tracer.rb
/usr/lib64/ruby/2.3.0/tsort.rb
/usr/lib64/ruby/2.3.0/un.rb
/usr/lib64/ruby/2.3.0/unicode_normalize.rb
/usr/lib64/ruby/2.3.0/uri.rb
/usr/lib64/ruby/2.3.0/weakref.rb
/usr/lib64/ruby/2.3.0/webrick.rb
/usr/lib64/ruby/2.3.0/xmlrpc.rb
/usr/lib64/ruby/2.3.0/yaml.rb
/usr/lib64/ruby/2.3.0/cgi/*
/usr/lib64/ruby/2.3.0/digest/sha2.rb
/usr/lib64/ruby/2.3.0/drb/*
/usr/lib64/ruby/2.3.0/fiddle/*
/usr/lib64/ruby/2.3.0/irb/*
/usr/lib64/ruby/2.3.0/matrix/*
/usr/lib64/ruby/2.3.0/net/*
/usr/lib64/ruby/2.3.0/openssl/*
/usr/lib64/ruby/2.3.0/optparse/*
/usr/lib64/ruby/2.3.0/racc/parser.rb
/usr/lib64/ruby/2.3.0/rbconfig/datadir.rb
/usr/lib64/ruby/2.3.0/rexml/*
/usr/lib64/ruby/2.3.0/rinda/*
/usr/lib64/ruby/2.3.0/ripper/*
/usr/lib64/ruby/2.3.0/rss/*
/usr/lib64/ruby/2.3.0/shell/*
/usr/lib64/ruby/2.3.0/syslog/logger.rb
/usr/lib64/ruby/2.3.0/uri/*
/usr/lib64/ruby/2.3.0/unicode_normalize/*
/usr/lib64/ruby/2.3.0/webrick/*
/usr/lib64/ruby/2.3.0/xmlrpc/*
/usr/lib64/ruby/2.3.0/yaml/*
%exclude /usr/lib64/ruby/gems/2.3.0/cache/
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/rbconfig.rb

%files bin
%defattr(-,root,root,-)
/usr/bin/erb
/usr/bin/irb
/usr/bin/ruby

%files data
%defattr(-,root,root,-)
/usr/share/ri/2.3.0/system/*

%files dev
%defattr(-,root,root,-)
/usr/include/ruby-2.3.0/*
/usr/lib64/pkgconfig/ruby-2.3.pc
/usr/lib64/libruby.so
/usr/lib64/libruby.so.2.3
/usr/lib64/libruby.so.2.3.0

%files doc
%defattr(-,root,root,-)
/usr/share/man/man1/erb.1
/usr/share/man/man1/irb.1
/usr/share/man/man1/ruby.1

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/cgi/escape.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/continuation.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/coverage.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/date_core.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/dbm.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/digest.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/digest/*.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/enc/*
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/etc.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/fcntl.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/fiber.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/fiddle.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/gdbm.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/mathn/*.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/nkf.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/objspace.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/openssl.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/pathname.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/pty.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/racc/cparse.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/readline.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/rbconfig/sizeof.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/ripper.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/sdbm.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/socket.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/stringio.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/strscan.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/syslog.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/thread.so
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/zlib.so

# Files included in rubygems package
%exclude /usr/bin/gem
%exclude /usr/lib64/ruby/2.3.0/rubygems/*
%exclude /usr/lib64/ruby/2.3.0/rubygems.rb
%exclude /usr/lib64/ruby/2.3.0/ubygems.rb
%exclude /usr/share/ri/2.3.0/system/Gem/*

%files -n rubygem-bigdecimal
%defattr(-,root,root,-)
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/bigdecimal.so
/usr/lib64/ruby/2.3.0/bigdecimal/*
/usr/share/ri/2.3.0/system/BigDecimal/*
/usr/lib64/ruby/gems/2.3.0/specifications/default/bigdecimal-1.2.8.gemspec

%files -n rubygem-did_you_mean
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/gems/did_you_mean-1.0.0/
/usr/lib64/ruby/gems/2.3.0/specifications/did_you_mean-1.0.0.gemspec

%files -n rubygem-io-console
%defattr(-,root,root,-)
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/io/*.so
/usr/lib64/ruby/2.3.0/io/console/size.rb
/usr/lib64/ruby/gems/2.3.0/specifications/default/io-console-0.4.5.gemspec

%files -n rubygem-json
%defattr(-,root,root,-)
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/json/ext/*.so
/usr/lib64/ruby/2.3.0/json
/usr/lib64/ruby/2.3.0/json.rb
/usr/share/ri/2.3.0/system/JSON/*
/usr/lib64/ruby/gems/2.3.0/specifications/default/json-1.8.3.gemspec

%files -n rubygem-minitest
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/specifications/minitest-5.8.3.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/minitest-5.8.3/

%files -n rubygem-net-telnet
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/gems/net-telnet-0.1.1/
/usr/lib64/ruby/gems/2.3.0/specifications/net-telnet-0.1.1.gemspec

%files -n rubygem-power_assert
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/specifications/power_assert-0.2.6.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/power_assert-0.2.6/

%files -n rubygem-psych
%defattr(-,root,root,-)
/usr/lib64/ruby/2.3.0/x86_64-linux-gnu/psych.so
/usr/lib64/ruby/2.3.0/psych/*
/usr/lib64/ruby/2.3.0/psych.rb
/usr/lib64/ruby/2.3.0/psych_jars.rb
/usr/share/ri/2.3.0/system/Psych/*
/usr/lib64/ruby/gems/2.3.0/specifications/default/psych-2.0.17.gemspec

%files -n rubygem-rake
%defattr(-,root,root,-)
/usr/bin/rake
/usr/lib64/ruby/gems/2.3.0/gems/rake-10.4.2/
/usr/share/ri/2.3.0/system/Rake/*
/usr/lib64/ruby/gems/2.3.0/specifications/rake-10.4.2.gemspec

%files -n rubygem-rdoc
%defattr(-,root,root,-)
/usr/bin/rdoc
/usr/bin/ri
/usr/share/man/man1/ri.1
/usr/lib64/ruby/2.3.0/rdoc/*
/usr/lib64/ruby/2.3.0/rdoc.rb
/usr/share/ri/2.3.0/system/RDocTask/*
/usr/share/ri/2.3.0/system/RDoc/*
/usr/lib64/ruby/gems/2.3.0/specifications/default/rdoc-4.2.1.gemspec
%exclude /usr/lib64/ruby/gems/2.3.0/gems/rdoc-4.2.1/bin/

%files -n rubygem-test-unit
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/specifications/test-unit-3.1.5.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/test-unit-3.1.5/
