# HOWTO Install a k3s cluster for the ARNEIS project

<!-- (2022-01-31 16:30 CET) -->

## Introduction

TODO

## References

* [K3S Installation](https://rancher.com/docs/k3s/latest/en/installation/) - from rancher.com/docs

## Prerequisites

* Administrative login to host (physical or virtual) with the following minimum requirements
  - CPU: min 2 cores
  - RAM: min 16 GiB
  - Disk: min 8 GiB SSD
  - OS: Ubuntu server 20.04 LTS
  - Fast internet connection (for updating OS and installing software)
  - Incoming ports: tcp/22 (SSH), TODO
  - Tested on arneis-vm01 (Virtual Machine on Azure Cloud - See [documentation](howto-create-vm-on-azure.md))

## Step-by-step instructions

Logged in as root@arneis-vm01, install k3s

```bash
curl -sfL https://get.k3s.io | sh -
```

Result:

```text
root@arneis-vm01:~# curl -sfL https://get.k3s.io | sh -
[INFO]  Finding release for channel stable
[INFO]  Using v1.22.5+k3s1 as release
[INFO]  Downloading hash https://github.com/k3s-io/k3s/releases/download/v1.22.5+k3s1/sha256sum-amd64.txt
[INFO]  Downloading binary https://github.com/k3s-io/k3s/releases/download/v1.22.5+k3s1/k3s
[INFO]  Verifying binary download
[INFO]  Installing k3s to /usr/local/bin/k3s
[INFO]  Skipping installation of SELinux RPM
[INFO]  Creating /usr/local/bin/kubectl symlink to k3s
[INFO]  Creating /usr/local/bin/crictl symlink to k3s
[INFO]  Creating /usr/local/bin/ctr symlink to k3s
[INFO]  Creating killall script /usr/local/bin/k3s-killall.sh
[INFO]  Creating uninstall script /usr/local/bin/k3s-uninstall.sh
[INFO]  env: Creating environment file /etc/systemd/system/k3s.service.env
[INFO]  systemd: Creating service file /etc/systemd/system/k3s.service
[INFO]  systemd: Enabling k3s unit
Created symlink /etc/systemd/system/multi-user.target.wants/k3s.service → /etc/systemd/system/k3s.service.
[INFO]  systemd: Starting k3s
root@arneis-vm01:~#
```

Verify that after a few minutes all the k3s services are up and running

```bash
kubectl get nodes
kubectl get all --all-namespaces
```

Result

```text
root@arneis-vm01:~# kubectl get all --all-namespaces
NAMESPACE     NAME                                         READY   STATUS      RESTARTS   AGE
kube-system   pod/coredns-85cb69466-7gm6x                  1/1     Running     0          2m49s
kube-system   pod/metrics-server-9cf544f65-ztddz           1/1     Running     0          2m49s
kube-system   pod/local-path-provisioner-64ffb68fd-g4cgw   1/1     Running     0          2m49s
kube-system   pod/helm-install-traefik-crd--1-fgbjx        0/1     Completed   0          2m50s
kube-system   pod/helm-install-traefik--1-w6c9h            0/1     Completed   2          2m50s
kube-system   pod/svclb-traefik-bdvfw                      2/2     Running     0          2m11s
kube-system   pod/traefik-786ff64748-9w7v6                 1/1     Running     0          2m12s

NAMESPACE     NAME                     TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)                      AGE
default       service/kubernetes       ClusterIP      10.43.0.1      <none>        443/TCP                      3m4s
kube-system   service/kube-dns         ClusterIP      10.43.0.10     <none>        53/UDP,53/TCP,9153/TCP       3m
kube-system   service/metrics-server   ClusterIP      10.43.46.89    <none>        443/TCP                      2m59s
kube-system   service/traefik          LoadBalancer   10.43.193.71   10.0.0.4      80:32593/TCP,443:30697/TCP   2m12s

NAMESPACE     NAME                           DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
kube-system   daemonset.apps/svclb-traefik   1         1         1       1            1           <none>          2m11s

NAMESPACE     NAME                                     READY   UP-TO-DATE   AVAILABLE   AGE
kube-system   deployment.apps/coredns                  1/1     1            1           3m
kube-system   deployment.apps/metrics-server           1/1     1            1           3m
kube-system   deployment.apps/local-path-provisioner   1/1     1            1           3m
kube-system   deployment.apps/traefik                  1/1     1            1           2m12s

NAMESPACE     NAME                                               DESIRED   CURRENT   READY   AGE
kube-system   replicaset.apps/coredns-85cb69466                  1         1         1       2m49s
kube-system   replicaset.apps/metrics-server-9cf544f65           1         1         1       2m49s
kube-system   replicaset.apps/local-path-provisioner-64ffb68fd   1         1         1       2m49s
kube-system   replicaset.apps/traefik-786ff64748                 1         1         1       2m12s

NAMESPACE     NAME                                 COMPLETIONS   DURATION   AGE
kube-system   job.batch/helm-install-traefik-crd   1/1           23s        2m58s
kube-system   job.batch/helm-install-traefik       1/1           39s        2m58s
root@arneis-vm01:~#
```

TODO

<!-- EOF -->
