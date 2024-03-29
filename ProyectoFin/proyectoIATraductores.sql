PGDMP     /    9                {            proyectoIATraductores    13.2    13.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    140237    proyectoIATraductores    DATABASE     t   CREATE DATABASE "proyectoIATraductores" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Mexico.1252';
 '   DROP DATABASE "proyectoIATraductores";
                postgres    false            �            1259    140251    juego    TABLE     j   CREATE TABLE public.juego (
    id_juego integer NOT NULL,
    id_participante integer,
    fecha date
);
    DROP TABLE public.juego;
       public         heap    postgres    false            �            1259    140249    juego_id_juego_seq    SEQUENCE     �   CREATE SEQUENCE public.juego_id_juego_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.juego_id_juego_seq;
       public          postgres    false    203            �           0    0    juego_id_juego_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.juego_id_juego_seq OWNED BY public.juego.id_juego;
          public          postgres    false    202            �            1259    140243    participante    TABLE     �   CREATE TABLE public.participante (
    id_participante integer NOT NULL,
    nombre character varying(50),
    edad integer,
    etiqueta character varying(20)
);
     DROP TABLE public.participante;
       public         heap    postgres    false            �            1259    140241     participante_id_participante_seq    SEQUENCE     �   CREATE SEQUENCE public.participante_id_participante_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public.participante_id_participante_seq;
       public          postgres    false    201            �           0    0     participante_id_participante_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public.participante_id_participante_seq OWNED BY public.participante.id_participante;
          public          postgres    false    200            �            1259    140270 	   resultado    TABLE     �   CREATE TABLE public.resultado (
    id_juego integer,
    id_participante integer,
    iteracion integer,
    seleccion character varying(1),
    ganancia integer,
    perdida integer,
    total integer
);
    DROP TABLE public.resultado;
       public         heap    postgres    false            -           2604    140254    juego id_juego    DEFAULT     p   ALTER TABLE ONLY public.juego ALTER COLUMN id_juego SET DEFAULT nextval('public.juego_id_juego_seq'::regclass);
 =   ALTER TABLE public.juego ALTER COLUMN id_juego DROP DEFAULT;
       public          postgres    false    202    203    203            ,           2604    140246    participante id_participante    DEFAULT     �   ALTER TABLE ONLY public.participante ALTER COLUMN id_participante SET DEFAULT nextval('public.participante_id_participante_seq'::regclass);
 K   ALTER TABLE public.participante ALTER COLUMN id_participante DROP DEFAULT;
       public          postgres    false    200    201    201            1           2606    140256    juego juego_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.juego
    ADD CONSTRAINT juego_pkey PRIMARY KEY (id_juego);
 :   ALTER TABLE ONLY public.juego DROP CONSTRAINT juego_pkey;
       public            postgres    false    203            /           2606    140248    participante participante_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.participante
    ADD CONSTRAINT participante_pkey PRIMARY KEY (id_participante);
 H   ALTER TABLE ONLY public.participante DROP CONSTRAINT participante_pkey;
       public            postgres    false    201            4           2606    140278    resultado idjuego_fk    FK CONSTRAINT     z   ALTER TABLE ONLY public.resultado
    ADD CONSTRAINT idjuego_fk FOREIGN KEY (id_juego) REFERENCES public.juego(id_juego);
 >   ALTER TABLE ONLY public.resultado DROP CONSTRAINT idjuego_fk;
       public          postgres    false    204    203    2865            2           2606    140265    juego idparticipante_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.juego
    ADD CONSTRAINT idparticipante_fk FOREIGN KEY (id_participante) REFERENCES public.participante(id_participante);
 A   ALTER TABLE ONLY public.juego DROP CONSTRAINT idparticipante_fk;
       public          postgres    false    2863    203    201            3           2606    140273    resultado idparticipante_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.resultado
    ADD CONSTRAINT idparticipante_fk FOREIGN KEY (id_participante) REFERENCES public.participante(id_participante);
 E   ALTER TABLE ONLY public.resultado DROP CONSTRAINT idparticipante_fk;
       public          postgres    false    2863    201    204           