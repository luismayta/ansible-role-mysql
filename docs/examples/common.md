<!-- Space: Projects -->
<!-- Parent: AnsibleRoleMySQL -->
<!-- Title: Examples AnsibleRoleMySQL -->
<!-- Label: Examples -->
<!-- Include: ./../disclaimer.md -->
<!-- Include: ac:toc -->

## packages

To run this playbook with default settings, for install package like this:

generate file `requirements.yml`

```yaml
- name: hadenlabs.ansible-role-mysql
  src: git+https://github.com/hadenlabs/ansible-role-mysql
  version: /main
```

```yaml
- hosts: all
  roles:
    - role: hadenlabs.ansible-role-mysql
      become: true
      vars:
        ansible-role-mysql_owner: ubuntu
```
